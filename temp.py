import os

folder = "audio"
species_set = set()

for f in os.listdir(folder):
    if f.endswith("_real.wav"):
        species_set.add(f.replace("_real.wav", ""))

for species in sorted(species_set):
    pretty_name = species.replace("Dolphin", " Dolphin") \
                         .replace("Whale", " Whale") \
                         .replace("Seal", " Seal") \
                         .replace("Walrus", " Walrus")

    print(f"""
<tr>
  <td>{pretty_name}</td>
  <td><audio controls src="audio/{species}_real.wav"></audio></td>
  <td><audio controls src="audio/{species}_dac.wav"></audio></td>
  <td><audio controls src="audio/{species}_snac.wav"></audio></td>
  <td><audio controls src="audio/{species}_encodec.wav"></audio></td>
  <td><audio controls src="audio/{species}_soundstream.wav"></audio></td>
</tr>
""")
