import random


class MenuPlanner:
    def __init__(self, menu, daily_budget):
        self.menu = menu
        self.daily_budget = daily_budget
        self.weekly_budget = daily_budget * 4
        self.monthly_budget = self.weekly_budget * 4

    def _select_random_dish(self, available_dishes, remaining_budget):
        """Select a random dish that fits within the remaining budget."""
        dish = random.choice(available_dishes)
        cost = self.menu[dish]
        if cost <= remaining_budget:
            return dish, cost
        return None, None

    def _plan_weekly_menu(self):
        """Plan a menu for a week."""
        weekly_menu = []
        remaining_budget = self.weekly_budget - self.menu['jugo']  # One juice a week
        available_dishes = [dish for dish, cost in self.menu.items() if dish != 'jugo']

        for _ in range(4):
            dish, cost = self._select_random_dish(available_dishes, remaining_budget)
            if dish:
                weekly_menu.append(dish)
                remaining_budget -= cost
                available_dishes.remove(dish)

        weekly_menu.append('jugo')
        return weekly_menu

    def plan_monthly_menu(self):
        """Plan a menu for a month."""
        monthly_menu = [self._plan_weekly_menu() for _ in range(4)]
        return monthly_menu