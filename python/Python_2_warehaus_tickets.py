# Copyright (c) 2025 Simona Schnitzer
# Licensed under the MIT License. See LICENSE file for details.
# ----- WAREHAUS TICKETS RESOLVER -----
# This script goes through a list of warehaus and closes any open tickets as resolved. 
# It shows the status for each resolved ticket. At the end, shows the total remaining open tickets.

warehaus_types =["Automated small parts Warenhaus", 
                "Manual warenhaus", "Shuttle system",
                "Production buffer warenhaus", 
                "Refrigeration systems", "Customized system"]

tickets = {"Automated small parts Warenhaus": True, 
                "Manual warenhaus": False, "Shuttle system": True, # True - means ticket open
                "Production buffer warenhaus": True,
                "Refrigeration systems": False, "Customized system": True}

for warehaus in warehaus_types:
    if tickets[warehaus]:
        tickets[warehaus] = False # means ticket is just resolved
        status = "resolved"
        print(f"Warehause: {warehaus}\n - tickets status: {status}\n")

open_tickets = sum(tickets.values())
print(f"Open tickets remaining: {open_tickets}") # how many tickets stays open

        

    