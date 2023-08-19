import torch
from transformers import AutoTokenizer, DistilBertForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Vineetttt/compliance_monitoring_oms")
model = DistilBertForSequenceClassification.from_pretrained("Vineetttt/compliance_monitoring_oms")

tokenizer.save_pretrained("model/tokenizer")
model.save_pretrained("model/saved_model")
