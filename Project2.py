import sys
sys.path.append('../resource/lib/public')
sys.path.append('../resource/asnlib/public')

# import pandapower
import pandapower
import pandapower.networks
import pandapower.topology
import pandapower.plotting
import pandapower.converter
import pandapower.estimation
import pandapower as pp
import pandas as pd

# import the network module
import pandapower.networks as pn

# import the packages needed for plotting of case 118, 1354
import pandapower.plotting as plot
import pandapower.networks as nw
import matplotlib.pyplot as plt


# store case 9 as 'net'
net = pn.case9()

# Run Power Flow
pp.runpp(net)

# Display the results of every bus
print("\n--- Bus Parameters ---")
print(net.bus)

print("\n--- Bus Results ---")
print(net.res_bus)

# Calculate and display total active power balance
total_power_balance = net.res_bus['p_mw'].sum()
print("\n Net active power balance (MW):", total_power_balance)

# Interpretation
if total_power_balance > 0:
    print("Result: More power is CONSUMED than produced.")
elif total_power_balance < 0:
    print("Result: More power is PRODUCED than consumed.")
else:
    print("Result: Perfect balance between production and consumption.")

# Display the results of power cables (lines)
print("\n--- Line Results ---")
print(net.res_line)

print("\n Total active power losses (MW):", net.res_line['pl_mw'].sum())

# store the case 118 network in a new variable 'net2'
net2 = pn.case118()

# it is more convenient to visualie the results in graphs, of big networks
print("\n The 118-bus test network",net2)

# Plot of net2
plot.simple_plot(net2, show_plot=False)  # don't auto-show inside simple_plot

# Add a title
plt.figtext(0.5, 0.01, "This is the visualisation of the 118 bus network.", ha='center', fontsize=12)


plt.show()
