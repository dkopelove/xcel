

class Residential:
    def __init__(self):
        self.service_and_facility_charge = 5.41
        self.production_meter_charge = 0.0
        self.windsource_charge = 0.015
        self.trans_cost_adj = .00109
        self.electric_commodity_adj = 0.02591
        self.dmd_side_mgmt = 0.00151
        self.purchase_cap_cost_adj = .00465
        self.cacja = .00503
        self.summer = False

    def calculate_price(self, energy_consumed):
        print()
        price = self.service_and_facility_charge
        print(f"Service & Facility: {self.service_and_facility_charge:.2f}")
        if self.summer:
            tier1 = min(energy_consumed, 500) * self.rates[0]
            price += tier1
            print(f"Tier1: {tier1:.2f}")
            tier2 = max(0, energy_consumed - 500) * self.rates[1]
            price += tier2
            print(f"Tier2: {tier2:.2f}")
        else:
            tier1 = energy_consumed * self.rates[0]
            price += tier1
            print(f"Tier1: {tier1:.2f}")
        wind = energy_consumed * self.windsource_charge
        price += wind
        print(f"Windsource: {wind:.2f}")
        tca = energy_consumed * self.trans_cost_adj
        price += tca
        print(f"Trans Cost Adj: {tca:.2f}")
        elec_adj = energy_consumed * self.electric_commodity_adj
        price += elec_adj
        print(f"Electric Commodity Adj: {elec_adj:.2f}")
        dmd_side_mgmt = energy_consumed * self.dmd_side_mgmt
        price += dmd_side_mgmt
        print(f"Demand Side Mgmt: {dmd_side_mgmt:.2f}")
        purchase_cap_cost = energy_consumed * self.purchase_cap_cost_adj
        price += purchase_cap_cost
        print(f"Purch Cap Cost Adj: {purchase_cap_cost:.2f}")
        cacja = energy_consumed * self.cacja
        price += cacja
        print(f"CACJA: {cacja:.2f}")
        return price


class ResidentialSummer(Residential):
    def __init__(self):
        super().__init__()
        self.rates = [0.05461, 0.09902]
        self.summer = True


class ResidentialWinter(Residential):
    def __init__(self):
        super().__init__()
        self.rates = [0.05461]


class RDTDR:
    def __init__(self):
        self.service_and_facility_charge = 5.41
        self.production_meter_charge = 0.00
        self.energy_charge = 0.00461
        self.distribution = 3.65
        self.ECA_on_peak = -30000
        self.ECA_off_peak = -30000
        self.generation_and_transmission_demand = -500
        self.windsource_charge = 0.015
        self.trans_cost_adj = .33
        self.dmd_side_mgmt = .34
        self.purch_cap_cost = .94
        self.cacja = .63
        # self.renewable_energy_adj = 1.83
        # self.GRSA = -2.55
        self.renewable_energy_adj = 0.0
        self.GRSA = 0.0

    def calculate_price(self, on_used, off_used, d, gt):
        print()
        price = self.service_and_facility_charge + self.production_meter_charge
        total_used = on_used + off_used
        print(f"Service & facility: {price:.2f}")
        res_dmd = total_used * self.energy_charge
        price += res_dmd
        print(f"RDTDR res dmd {res_dmd:.2f}")
        eca_on = self.ECA_on_peak * on_used
        price += eca_on
        print(f"ECA on: {eca_on:.2f}")
        eca_off = self.ECA_off_peak * off_used
        price += eca_off
        print(f"ECA off: {eca_off:.2f}")
        wind = total_used * self.windsource_charge
        price += wind
        print(f"Windsource: {wind:.2f}")
        dmd = d * self.distribution
        price += dmd
        print(f"Demand: {dmd:.2f}")
        g_and_t = gt * self.generation_and_transmission_demand
        price += g_and_t
        print(f"Generation and Demand: {g_and_t:.2f}")
        tca = gt * self.trans_cost_adj
        price += tca
        print(f"Trans Cost Adj: {tca:.2f}")
        dmd_side_mgmt = gt * self.dmd_side_mgmt
        price += dmd_side_mgmt
        print(f"Demand Side Mgmt: {dmd_side_mgmt:.2f}")
        purchase_cap_cost = gt * self.purch_cap_cost
        price += purchase_cap_cost
        print(f"Purchase Cap Cost: {purchase_cap_cost:.2f}")
        cacja = gt * self.cacja
        price += cacja
        print(f"CACJA: {cacja:.2f}")
        price += self.renewable_energy_adj + self.GRSA
        return price


class RDTDRSummer(RDTDR):
    def __init__(self):
        super().__init__()
        self.generation_and_transmission_demand = 9.73
        # self.ECA_on_peak = .02999
        self.ECA_on_peak = .033870
        # self.ECA_off_peak = .02054
        self.ECA_off_peak = .0232


class RDTDRWinter(RDTDR):
    def __init__(self):
        super().__init__()
        self.generation_and_transmission_demand = 6.81
        self.ECA_on_peak = .04065
        self.ECA_off_peak = .02784


class RETOU:
    def __init__(self):
        self.service_and_facility_charge = 5.41
        self.production_meter_charge = 0.00
        self.windsource_charge = 0.015
        self.trans_cost_adj = .00109
        self.electric_commodity_adj = 0.02591
        self.dmd_side_mgmt = 0.00151
        self.purchase_cap_cost_adj = .00465
        self.cacja = .00503
        self.summer = False
        self.on_peak = 0.0
        self.off_peak = 0.0
        self.shoulder = 0.0

    def calculate_price(self, on, off, shoulder):
        print()
        price = self.service_and_facility_charge
        print(f"Service & Facility: {self.service_and_facility_charge:.2f}")
        on_cost = on * self.on_peak
        price += on_cost
        print(f"On usage: {on_cost:.2f}")
        off_cost = off * self.off_peak
        price += off_cost
        print(f"Off usage: {off_cost:.2f}")
        shoulder_cost = shoulder * self.shoulder
        price += shoulder_cost
        print(f"Shoulder usage: {shoulder_cost:.2f}")
        energy_consumed = on + off + shoulder
        wind = energy_consumed * self.windsource_charge
        price += wind
        print(f"Windsource: {wind:.2f}")
        tca = energy_consumed * self.trans_cost_adj
        price += tca
        print(f"Trans Cost Adj: {tca:.2f}")
        elec_adj = energy_consumed * self.electric_commodity_adj
        price += elec_adj
        print(f"Electric Commodity Adj: {elec_adj:.2f}")
        dmd_side_mgmt = energy_consumed * self.dmd_side_mgmt
        price += dmd_side_mgmt
        print(f"Demand Side Mgmt: {dmd_side_mgmt:.2f}")
        purchase_cap_cost = energy_consumed * self.purchase_cap_cost_adj
        price += purchase_cap_cost
        print(f"Purch Cap Cost Adj: {purchase_cap_cost:.2f}")
        cacja = energy_consumed * self.cacja
        price += cacja
        print(f"CACJA: {cacja:.2f}")
        return price


class RETOUSummer(RETOU):
    def __init__(self):
        super().__init__()
        self.on_peak = .13814
        self.off_peak = 0.0444
        self.shoulder = .08420

class RETOUWinter(RETOU):
    def __init__(self):
        super().__init__()
        self.on_peak = .0888
        self.off_peak = .0444
        self.shoulder = .05413
