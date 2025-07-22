spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")

# Initial spice mix id: 2152639628000
# Initial spice mix: set()
# Initial spice mix id: {'Cardamom', 'Ginger'}
# After spice mix id: 2152639628000