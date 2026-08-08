#!/usr/bin/env python3
"""
BATNA / ZOPA calculator: computes the zone of possible agreement between
your reservation price and the counterparty's estimated reservation price,
recommends an anchor, and flags when no ZOPA exists (in which case the
right move is walking away or changing the deal structure, not negotiating
harder on price).

Usage:
    python3 batna_zopa.py --config negotiation.json

negotiation.json shape:
{
  "role": "buyer",
  "your_target_price": 400000,
  "your_batna_value": 480000,
  "counterparty_estimated_reservation_price": 460000,
  "counterparty_estimated_target_price": 420000
}
role: "buyer" or "seller". your_batna_value is what you get if this deal
falls through (your best alternative) — for a buyer, your reservation
price should never exceed your BATNA value; for a seller, it should never
go below it.
"""
import argparse
import json


def money(x):
    return f"${x:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    with open(args.config) as f:
        cfg = json.load(f)

    role = cfg["role"]
    target = cfg["your_target_price"]
    batna = cfg["your_batna_value"]
    cp_reservation = cfg["counterparty_estimated_reservation_price"]
    cp_target = cfg.get("counterparty_estimated_target_price")

    print("=== BATNA / ZOPA Analysis ===\n")
    print(f"Your role: {role}")
    print(f"Your target price: {money(target)}")
    print(f"Your BATNA value (walk-away point): {money(batna)}")
    print(f"Counterparty's estimated reservation price: {money(cp_reservation)}")

    if role == "buyer":
        your_reservation = batna  # never pay more than your BATNA
        zopa_low = cp_reservation   # seller won't go below their reservation
        zopa_high = your_reservation  # you won't go above yours
        zopa_exists = zopa_high >= zopa_low
        print(f"\nYour implied reservation price (should not exceed BATNA): {money(your_reservation)}")
    else:  # seller
        your_reservation = batna  # never sell for less than your BATNA
        zopa_low = your_reservation
        zopa_high = cp_reservation
        zopa_exists = zopa_high >= zopa_low
        print(f"\nYour implied reservation price (should not go below BATNA): {money(your_reservation)}")

    if zopa_exists:
        print(f"\nZOPA (Zone of Possible Agreement): {money(zopa_low)} to {money(zopa_high)}")
        zopa_midpoint = (zopa_low + zopa_high) / 2
        print(f"ZOPA midpoint: {money(zopa_midpoint)}")

        if role == "buyer":
            anchor = max(target, zopa_low)
            print(f"\nRecommended opening anchor: {money(anchor)}")
            print("As buyer, anchor near or slightly below your target, but inside the ZOPA")
            print("so the opening offer is taken seriously rather than dismissed as a bad-faith move.")
        else:
            anchor = min(target, zopa_high)
            print(f"\nRecommended opening anchor: {money(anchor)}")
            print("As seller, anchor near or slightly above your target, but inside the ZOPA.")

        print(f"\nYour walk-away price: {money(your_reservation)} (this is your BATNA, not a")
        print("negotiating tactic — going past it means the deal destroys value versus your")
        print("actual alternative, regardless of how the conversation feels in the room).")
    else:
        gap = zopa_low - zopa_high if role == "buyer" else zopa_low - zopa_high
        print(f"\n>>> NO ZOPA EXISTS. Your reservation price and the counterparty's estimated")
        print(f"    reservation price do not overlap by an estimated {money(abs(gap))}.")
        print("    Negotiating harder on price will not close a gap this size. Either:")
        print("    (a) the deal should not happen at current terms, walk away to your BATNA,")
        print("    (b) change the deal structure (financing, timeline, scope) to create value")
        print("        that shifts one side's reservation price, or")
        print("    (c) your estimate of their reservation price may be wrong — verify before")
        print("        concluding no deal is possible.")

    if cp_target:
        print(f"\nCounterparty's estimated target price: {money(cp_target)}")
        print("Treat this as the number they'll open near, not what they'll actually accept.")


if __name__ == "__main__":
    main()
