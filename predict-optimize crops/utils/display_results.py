def display_optimal_allocation(crops, best_solution, cost_per_m2, weight_area, revenue_per_m2, total_area, total_budget):
    total_cost = 0
    total_expected_weight_return = 0
    total_expected_money_return = 0
    total_area_used = 0

    print("\nOptimal allocation and expected returns:")
    for i, crop in enumerate(crops):
        area_for_crop = best_solution[i]
        cost_for_crop = area_for_crop * cost_per_m2[i]
        expected_weight_return = area_for_crop * weight_area[i]
        expected_money_return = area_for_crop * revenue_per_m2[i]
        
        total_cost += cost_for_crop
        total_expected_weight_return += expected_weight_return
        total_expected_money_return += expected_money_return
        total_area_used += area_for_crop
        
        if area_for_crop > 0:
            print(f"{crop}:")
            print(f"  Area: {area_for_crop} m²")
            print(f"  Expected return in weight: {expected_weight_return:.2f} units")
            print(f"  Expected return in money: ${expected_money_return:.2f}")
            print(f"  Cost: ${cost_for_crop:.2f}")
            print()

    total_profit = total_expected_money_return - total_cost

    print(f"Total area used: {total_area_used} m² out of {total_area} m²")
    print(f"Unused area: {total_area - total_area_used} m²")
    print(f"Total expected return in money: ${total_expected_money_return:.2f}")
    print(f"Total expected return in weight: {total_expected_weight_return:.2f} units")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Total profit: ${total_profit:.2f}")
    print(f"Budget utilization: {(total_cost / total_budget) * 100:.2f}%")
