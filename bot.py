from mastodon import Mastodon
import random

# Configuration Mastodon avec VOTRE TOKEN
mastodon = Mastodon(
    access_token="PUOHFBFDolC4ZKDJseYmRBKa2imeciJjbupZH14BsTk",  # Token collé ici
    api_base_url="https://mastodon.social"  # Changez si vous utilisez une autre instance
)

# Liste de citations (personnalisable)
citations = [
    "« Le courage n'est pas l'absence de peur, mais la capacité de la vaincre. » - Nelson Mandela",
    "« La simplicité est la sophistication suprême. » - Léonard de Vinci",
    "« Votre temps est limité, ne le gâchez pas à vivre la vie de quelqu'un d'autre. » - Steve Jobs"
]

# Poste une citation aléatoire
try:
    citation = random.choice(citations)
    mastodon.toot(citation)
    print("✅ Citation postée avec succès :\n" + citation)
except Exception as e:
    print("❌ Erreur :", e)