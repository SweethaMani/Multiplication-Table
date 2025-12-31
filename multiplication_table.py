def multiplication_table():
    print("   ", end="") 
    for i in range(1, 13):
        print(f"{i:4}", end="")
    print()

    print("  :" + "-" * 48)

    for row in range(1, 13):
        print(f"{row:2}:", end="")
        for col in range(1, 13):
            print(f"{col * row:4}", end="")
        print()
print("Multiplication Table:")
multiplication_table()