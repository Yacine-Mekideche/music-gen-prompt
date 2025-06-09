import torch
import torchaudio
from audiocraft.models import MusicGen

def generate_music(prompt: str, duration: int = 10, output_path: str = "output.wav") -> str:
    """
    Génère une musique à partir d’un prompt texte.

    Args:
        prompt (str): Description textuelle.
        duration (int): Durée en secondes.
        output_path (str): Chemin du fichier .wav.

    Returns:
        str: Chemin du fichier audio généré.
    """
    print("🎼 Chargement du modèle MusicGen...")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"⚠️ GPU {'disponible' if device == 'cuda' else 'non disponible'}, utilisation du {device}.")

    model = MusicGen.get_pretrained('facebook/musicgen-small')
    model.set_generation_params(duration=duration)

    # Déplacer les sous-modèles sur le bon device
    model.lm.to(device)
    model.compression_model.to(device)

    print("⏳ Génération en cours...")
    wav = model.generate([prompt], progress=True)

    sample_rate = model.sample_rate
    torchaudio.save(output_path, wav[0].cpu(), sample_rate)

    print(f"✅ Fichier audio sauvegardé : {output_path}")
    return output_path
