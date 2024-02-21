from simulation.inventory_simulation import InventorySimulation

def avg(lst):
    return sum(lst) / len(lst)

def main():
    media_list = []
    for _ in range(30):
        simulation = InventorySimulation()
        media_list.append(avg(simulation.simulate()))
    print(avg(media_list))

if __name__ == "__main__":
    main()