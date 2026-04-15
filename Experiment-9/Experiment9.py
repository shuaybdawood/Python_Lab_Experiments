import pandas as pd
import matplotlib.pyplot as plt

# data
Points = [180, 165, 150, 140, 130, 120, 110, 100, 95, 90]
Teams = ["Ducati", "Pramac", "Repsol Honda", "Yamaha", "KTM", "Aprilia", "LCR Honda", "GasGas", "VR6", "RNF Yamaha"]

# dataframe
df = pd.DataFrame({
    "Points": Points,
    "Teams": Teams
})

print(df)

# plotting
plt.figure()
plt.plot(Teams, Points)
plt.title("MotoGP Team Points")
plt.xlabel("Teams")
plt.ylabel("Points")
plt.show()