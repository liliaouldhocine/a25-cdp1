from memory.memory import Memory

def main():
    mem = Memory()
    mem.store("A", 10)
    print(mem.read("A"))  # 10
    mem.clear("A")
    print(mem.read("A"))  # None

if __name__ == "__main__":
    main()
