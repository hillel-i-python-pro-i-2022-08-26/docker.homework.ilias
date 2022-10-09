from faker import Faker

fake = Faker()


def stroke():
    print(
        f"Hello my name is {fake.first_name()} and my 2nd name is {fake.name().split()[1]} "
    )


if __name__ == "__main__":
    stroke()
