from submodule_one import SubmoduleOne
from submodule_two import SubmoduleTwo


def main():
    s1 = SubmoduleOne()
    s1.report()

    s2 = SubmoduleTwo()
    s2.report()

if __name__ == "__main__":
    main()
