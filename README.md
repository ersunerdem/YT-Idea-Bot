# YT-Idea-Bot

## Project Description:

Uses Google's YouTube API to gather info (video titles and descriptions) and then generates titles (and soon descriptions) from that using a keras model.

## How to Install and Run:
Fork this project and register with Google's YouTube API. Then, acquire the API's .json file, and rename the file in yt-dataset-gen.py to match. Edit search terms in yt-dataset-gen.py.

If youtube_data.txt, training_data.txt, and text_data.txt all exist, delete them. Then run yt-dataset-gen.py to recreate these files with the data from your personalized search.

After running yt-dataset-gen.py, run bot.py. This will train the bot with weights based on your generated data. Finally, it should output titles relevant to your searches.
(NOTE: This is still a SUPER early project and I'm messing around with the architecture of my model. As this project improves, the results should be more and more fine-tuned, but currently they may seem like gibberish.)

## Future Plans:

* Fine tune model architecture
* Add descriptions generator
* Ensure nextPageToken is working, so that more than 50 videos per search are appended to list

## Credits:

YouTube API: https://developers.google.com/youtube/v3

keras: https://keras.io/
