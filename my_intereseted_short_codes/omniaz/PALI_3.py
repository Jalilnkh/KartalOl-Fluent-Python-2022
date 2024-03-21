import torch
from pali3.main import Pali3
from zeta.nn import MLPMixer
#model = Pali3()
if __name__ == "__main__":
    # Example of creating a model instance
    mlp_mixer = MLPMixer(
        num_classes=10,
        num_blocks=8,
        patch_size=16,
        hidden_dim=512,
        tokens_mlp_dim=512,
        channels_mlp_dim=512,
    )

    # Example input tensor
    example_input = torch.randn(
        1, 512, 32, 32
    )  # Batch size of 1, 512 channels, 32x32 image
    output = mlp_mixer(example_input)
    print(
        output.shape
    )  # Should output the shape corresponding to the
"""img = torch.randn(1, 3, 256, 256)
prompt = torch.randint(0, 256, (1, 1024))
mask = torch.ones(1, 1024).bool()
output_text = torch.randint(0, 256, (1, 1024))

result = model.process(img, prompt, output_text, mask)
print(result)"""

