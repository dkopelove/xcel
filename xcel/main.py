import sys

from xcel.schedules import RDTDRWinter, ResidentialWinter, RDTDRSummer, ResidentialSummer, RETOUWinter, RETOUSummer


def print_sep():
    print("----------------------------------------------------------------------------")


def main():
    winter_RDTDR = RDTDRWinter()
    summer_RDTDR = RDTDRSummer()
    winter_res = ResidentialWinter()
    summer_res = ResidentialSummer()

    winter_retou = RETOUWinter()
    summer_retou = RETOUSummer()

    print_sep()

    winter_tdr_price = winter_RDTDR.calculate_price(603, 817, 12, 2)
    print(f"OCT 2018 on winter RDTDR: {winter_tdr_price:.2f}")
    winter_res_price = winter_res.calculate_price(1419)
    print(f"OCT 2018 on winter Res: {winter_res_price:.2f}")

    print_sep()

    summer_tdr_price = summer_RDTDR.calculate_price(281, 429, 9, 2)
    print(f"AUG 2018 on summer RDTDR: {summer_tdr_price:.2f}")
    summer_res_price = summer_res.calculate_price(710)
    print(f"AUG 2018 on summer residential: {summer_res_price:.2f}")

    print_sep()

    print("Experimental - winter - 1")
    print("1000kwh used, 9kw off, 2 on, 500 off, 500 on")
    winter_tdr_price = winter_RDTDR.calculate_price(500, 500, 9, 2)
    print(f"exp winter TDR: {winter_tdr_price:.2f}")

    winter_res_price = winter_res.calculate_price(1000)
    print(f"exp winter res: {winter_res_price:.2f}")

    print_sep()

    print("Experimental - winter - 2")
    print("2500kwh used, 9kw off, 2 on, 1000 on, 1500 off")
    winter_tdr_price = winter_RDTDR.calculate_price(1000, 1500, 9, 2)
    print(f"exp winter TDR: {winter_tdr_price:.2f}")

    winter_res_price = winter_res.calculate_price(2500)
    print(f"exp winter res: {winter_res_price:.2f}")

    print_sep()

    print("Experimental - winter - 3")
    tot = 3000
    on_frac = .2
    off_frac = 1-on_frac
    dmd = 9
    gt = 3

    print(f"{tot} kwh used, {dmd}kw off, {gt}kw on, {tot*on_frac} on, {tot*off_frac} off")
    winter_tdr_price = winter_RDTDR.calculate_price(tot*on_frac, tot*off_frac, dmd, gt)
    print(f"exp winter TDR: {winter_tdr_price:.2f}")

    winter_res_price = winter_res.calculate_price(tot)
    print(f"exp winter res: {winter_res_price:.2f}")

    print_sep()
    print_sep()

    print("Experimental - summer - 1")
    print("1500kwh used, 9kw off, 2 on, 700 on, 800 off")
    summer_tdr_price = summer_RDTDR.calculate_price(700, 800, 9, 2)
    print(f"exp summer TDR: {summer_tdr_price:.2f}")

    summer_res_price = summer_res.calculate_price(1500)
    print(f"exp summer res: {summer_res_price:.2f}")

    print_sep()

    print("Experimental - summer - 2")
    print("750kwh used, 9kw off, 2 on, 350 on, 400 off")
    summer_tdr_price = summer_RDTDR.calculate_price(350, 400, 9, 2)
    print(f"exp summer TDR: {summer_tdr_price:.2f}")

    summer_res_price = summer_res.calculate_price(750)
    print(f"exp summer res: {summer_res_price:.2f}")

    print_sep()
    print_sep()
    print_sep()
    dmd = 20
    gt = 7
    eca_on = 1128
    eca_off = 1537
    print(f"{tot} kwh used, {dmd}kw off, {gt}kw on, {eca_on} on, {eca_off} off")
    winter_tdr_price = winter_RDTDR.calculate_price(eca_on, eca_off, dmd, gt)
    print(f"exp winter TDR: {winter_tdr_price:.2f}")

    winter_res_price = winter_res.calculate_price(eca_on+eca_off)
    print(f"exp winter res: {winter_res_price:.2f}")

    print("")
    tot = 2665
    on = 200
    off = (tot-200)*2/3
    shoulder = (tot-200)/3
    winter_exp_price = winter_retou.calculate_price(on, off, shoulder)
    print(f"exp winter tou: {winter_exp_price:.2f}")

    print_sep()



if __name__ == '__main__':
    main()
