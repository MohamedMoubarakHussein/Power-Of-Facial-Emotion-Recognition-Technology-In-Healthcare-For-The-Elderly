import random

def chatGpt(mood):
    prompts = [f"act like an author and generate a full story which make my {mood} mood better and start the story with Once Upon a Time and give me the title of the story ",
                f" i feel {mood} mood recommend to me the list of 5 movies with overall idea of each one  which make my overall mood better and give it a good title and start  the response with there are 5 movies which make your {mood} better and make the title at the first of response",
                f"i feel {mood} mood recommed to me an 10 exercises which  make my mood better and give it a good title and start with there are 10 exercises which make your {mood} better and make the title at the first of response",
                f"i feel {mood} mood recommed to me an 10 habits  which  make my mood better and give it a good title and start with there are 10 habits which make your {mood} better and make the title at the first of response",
                f"i feel {mood} mood recommed to me an 10 advices which  make my mood better and give it a good title and start with there are 10 advices which make your {mood} better and make the title at the first of response"]
    prompt = random.sample(prompts,1)
    return prompt

def spotify():
    Positive_Playlists = ["37i9dQZF1DX7KNKjOK0o75","37i9dQZF1DXdPec7aLTmlC","37i9dQZF1DX3rxVfibe1L0",
                     "37i9dQZF1DWSkMjlBZAZ07","37i9dQZF1DWYBO1MoTDhZI","0RH319xCjeU8VyTSqCF6M4"
                     ,"37i9dQZF1DWTUHzPOW6Jl7","37i9dQZF1DWTXGqmP0bfT3","37i9dQZF1DWZVAVMhIe3pV",
                     "37i9dQZF1DWXLSRKeL7KwM","4tgaubXJZ9aC5eJ3lwcPQO","3J1xYs9dA2Jh7H1ujLJSOX"
                     ,"37i9dQZF1DWU0ScTcjJBdj","3XZa6C8tc7njNXn2PWRwQs","7jM62qbx0nLl82afAgU3kb"
                     "37i9dQZF1DXaImRpG7HXqp","1cgoc9PfTBMZlEYhHtGoWg","4D3hxAbOjVu5jaC5Bnlmky"
                     ,"37i9dQZF1DWUAZoWydCivZ","4Arnste28husOS9fbXKiPe","7v3Ab1w6OyMbf5Ixe5sD7F",
                     "4UQUAdUR7jyrCabpsqC5RE","51bWXcnDHBEWRzjL9MqPLm","37i9dQZF1DWYmSg58uBxin"]
    return  random.sample(Positive_Playlists, 1)

def image():
    prompts = ["A cozy cabin in the woods surrounded by tall trees with golden leaves. The cabin has a warm fire burning in the fireplace and comfortable chairs to relax in. Outside, there's a river flowing gently and a family of deer grazing nearby. The scene is peaceful and serene, making you feel relaxed and content.",
            "A futuristic cityscape with towering skyscrapers and flying cars zooming past. The buildings are illuminated with bright neon lights and there are holographic advertisements everywhere. In the distance, you can see a massive space station orbiting the planet. The scene is exhilarating and full of energy, making you feel excited and inspired.",
            "A magical forest with sparkling fairy lights hanging from the trees. The forest is filled with colorful mushrooms and friendly woodland creatures like squirrels, rabbits, and birds. In the center of the forest, there's a beautiful waterfall with a rainbow shining through. The scene is enchanting and whimsical, making you feel joyful and carefree.",
            "A sandy beach with turquoise waters and palm trees swaying in the breeze. There are comfortable lounge chairs and colorful umbrellas to relax under. In the distance, you can see a sailboat gliding across the water. The scene is tranquil and refreshing, making you feel relaxed and rejuvenated.",
            "A cozy coffee shop with comfortable chairs and a warm fireplace. The walls are lined with shelves full of books and there's a vintage record player playing soft jazz music. The barista is friendly and skilled, making delicious coffee drinks and homemade pastries. The scene is cozy and inviting, making you feel comfortable and happy.",
            "A snowy mountain with pristine white snow and a clear blue sky. There are ski slopes and a cozy lodge with a roaring fire and comfortable couches. In the distance, you can see a herd of elk grazing on the mountainside. The scene is peaceful and majestic, making you feel awe-inspired and calm.",
            "A bustling farmer's market with stalls selling fresh fruits, vegetables, and flowers. There's a lively band playing music and people laughing and chatting. The smells of freshly baked bread and roasted coffee fill the air. The scene is vibrant and full of life, making you feel energized and happy.",
            "A beautiful sunrise over a calm lake surrounded by mountains. The sky is painted with shades of pink, orange, and purple, and the water reflects the colors. There's a gentle mist rising off the lake, and the air is cool and fresh. The scene is peaceful and serene, making you feel calm and content.",
            "A calm lake surrounded by beautiful mountains with a soft orange and pink sunset in the background. There's a small boat on the lake with a person fishing, enjoying the peaceful scenery. The water is still and reflects the colors of the sky, creating a beautiful and serene atmosphere. The scene is quiet and peaceful, making you feel relaxed and calm.",
            "A beautiful garden with colorful flowers in full bloom. There's a gentle breeze blowing, and the flowers sway gently. The sun is shining, and the sky is blue. The scent of the flowers fills the air, creating a peaceful and relaxing atmosphere. The scene is vibrant and full of life, making you feel happy and calm.",
            "A peaceful forest with tall trees and a babbling brook. There's a soft green moss covering the ground, and the sun is filtering through the leaves. The birds are singing, and the sound of the water is soothing. The scene is tranquil and calming, making you feel at peace.",
            "A beautiful beach with crystal clear water and soft white sand. There's a gentle breeze blowing, and the waves are lapping at the shore. The sun is shining, and the sky is blue. There are palm trees swaying in the wind, and the sound of the waves is relaxing. The scene is refreshing and rejuvenating, making you feel calm and refreshed.",
            "A beautiful sunset over the ocean with shades of pink, orange, and purple in the sky. The water is calm, and the waves are gently lapping at the shore. There are seagulls flying overhead, and the sound of the waves is soothing. The scene is beautiful and calming, making you feel relaxed and happy.",
             "A beautiful park with trees, flowers, and a gentle stream. There are people walking along the paths, and children playing on the playground. The sun is shining, and the sky is blue. The sound of the water and the birds is soothing, and the scene is peaceful and relaxing, making you feel calm and happy.",
             "A peaceful meadow with tall grass and a clear blue sky. There are colorful butterflies and birds flying overhead, and the sound of chirping birds fills the air. The scene is tranquil and calming, making you feel safe and secure.",
             "A beautiful sunrise over a calm lake with mist rising off the water. There are tall trees in the distance, and the colors of the sky are reflected in the water. The scene is peaceful and serene, making you feel relaxed and calm.",
             "A cozy cabin in the woods surrounded by tall trees with golden leaves. The cabin has a warm fire burning in the fireplace and comfortable chairs to relax in. The scene is warm and inviting, making you feel safe and comfortable.",
             "A beautiful garden with colorful flowers in full bloom. There's a gentle breeze blowing, and the flowers sway gently. The scene is peaceful and calming, making you feel safe and secure.",
             "A peaceful forest with tall trees and a babbling brook. The birds are singing, and the sound of the water is soothing. The scene is tranquil and calming, making you feel safe and secure.",
             "A beautiful beach with crystal clear water and soft white sand. The sun is shining, and the sky is blue. The sound of the waves is soothing, and the scene is refreshing and rejuvenating, making you feel safe and secure.",
             "A beautiful sunset over the ocean with shades of pink, orange, and purple in the sky. The water is calm, and the waves are gently lapping at the shore. The scene is beautiful and calming, making you feel safe and secure.",
             "A beautiful park with trees, flowers, and a gentle stream. There are people walking along the paths, and children playing on the playground. The scene is peaceful and relaxing, making you feel safe and secure.",
             "A beautiful mountain range with tall peaks and a clear blue sky. The sun is shining, and the air is fresh and crisp. The scene is majestic and awe-inspiring, making you feel renewed and invigorated.",
             "A peaceful lake with a beautiful sunset in the background. The sky is painted with shades of pink, orange, and purple, and the water reflects the colors. The scene is calming and serene, making you feel relaxed and content.",
             "A beautiful park with trees, flowers, and a gentle stream. There are people walking along the paths, and children playing on the playground. The scene is peaceful and relaxing, making you feel renewed and hopeful.",
             "Joyful sunset sky","Cute puppy playing","Beautiful beach at sunrise","Colorful bouquet of tulips","Rainbow after a rain shower",
             "Kitten peeking out of a basket","Snowy mountain landscape","Starry night sky","Sandy desert dunes at dawn","Misty autumn forest",
             "Bird soaring in the blue sky","Whimsical dreamy clouds","Sparking glitter and confetti","Delicious chocolate cake",
             "Cheerful lemonade stand","Vintage carousel","Hot air balloons festival","Neon city lights at night","Lake louise with turquoise water",
             "Cascading waterfall in lush forest","photos of happy smiling people laughing together in harmony","pictures of golden sunrises over mountains",
            "images of cute puppies and kittens playing","landscape shots of sparkling beach waves hitting the shore at sunset",
            "pictures of kids hugging and playing in a park on a sunny afternoon","images of people embracing loved ones joyfully","picturesque pictures of flowers blossoming in springtime",
            "beautiful photographs of colorful butterflies fluttering","photos of people in love gazing into each other's eyes lovingly",
            "scenic shots of majestic snowcapped mountains under a clear blue sky"
            ]
    return random.sample(prompts, 1)

    