import os
from PIL import Image, ImageFile
from torch.utils.data import Dataset

ImageFile.LOAD_TRUNCATED_IMAGES = True

class CustomImageDataset(Dataset):
    def __init__(self, root_dir, transform=None, max_samples=None):
        self.root_dir = root_dir
        self.transform = transform
        self.classes = os.listdir(root_dir)
        print(self.classes)
        self.files = []
        for label in self.classes:
            class_files = [f for f in os.listdir(os.path.join(root_dir, label)) if f.endswith('.png')]
            if max_samples is not None:
                samples_per_class = max_samples // len(self.classes)
                self.files += [(f, label) for f in class_files[:samples_per_class]]
            else:
                self.files += [(f, label) for f in class_files]

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        img_name, label = self.files[idx]
        img_path = os.path.join(self.root_dir, label, img_name)
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image, self.classes.index(label)
