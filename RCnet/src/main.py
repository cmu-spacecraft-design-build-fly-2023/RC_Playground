import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, models
from PIL import Image
import yaml
import matplotlib.pyplot as plt
from region_classifier import ImageClassifier

if __name__ == "__main__":
    with open('config_region_classifier.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    train_flag = config['flags']['train_flag']
    save_plot_flag = config['flags']['save_plot_flag']
    save_plot_path = config['paths']['save_plot_path']
    train_path = config['paths']['train_path']
    test_path = config['paths']['test_path']
    val_path = config['paths']['val_path'] 
    
    
    classifier = ImageClassifier(train_path, test_path, save_plot_flag, save_plot_path, val_path)  
    if train_flag:
        classifier.train(epochs=config['hyperparameters']['epochs'],learning_rate=config['hyperparameters']['learning_rate'])
        classifier.save_model(path=config['paths']['model_save_path'])
    else:
        classifier.load_model(path=config['paths']['model_load_path'])
        print("Loading model")
    
    classifier.evaluate()
