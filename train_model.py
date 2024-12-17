from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, RandomSampler, TensorDataset
import torch
from sklearn.metrics import accuracy_score

def train_model(learning_rate, batch_size, epochs):
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Data dummy
    train_data = [("This is a positive example.", 1), ("This is a negative example.", 0)]
    texts, labels = zip(*train_data)
    encodings = tokenizer(list(texts), truncation=True, padding=True, max_length=512)
    inputs = torch.tensor(encodings['input_ids'])
    targets = torch.tensor(labels)

    dataset = TensorDataset(inputs, targets)
    train_sampler = RandomSampler(dataset)
    train_dataloader = DataLoader(dataset, sampler=train_sampler, batch_size=batch_size)

    optimizer = AdamW(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        model.train()
        all_preds = []
        all_labels = []
        for batch in train_dataloader:
            batch_input_ids, batch_labels = batch
            optimizer.zero_grad()

            # Forward pass
            outputs = model(batch_input_ids, labels=batch_labels)
            loss = outputs.loss
            logits = outputs.logits

            # Backward pass dan optimasi
            loss.backward()
            optimizer.step()

            # Simpan prediksi untuk menghitung akurasi
            preds = torch.argmax(logits, dim=-1).detach().cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(batch_labels.detach().cpu().numpy())

        # Hitung akurasi
        acc = accuracy_score(all_labels, all_preds)
        print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item()} - Accuracy: {acc}")

    return model

# Eksperimen dengan hyperparameter
learning_rates = [1e-5, 3e-5, 5e-5]
batch_sizes = [8, 16, 32]
epochs = 3

for lr in learning_rates:
    for batch_size in batch_sizes:
        print(f"Training with Learning Rate: {lr}, Batch Size: {batch_size}")
        trained_model = train_model(lr, batch_size, epochs)
