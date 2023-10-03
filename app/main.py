from menu_planner import MenuPlanner
from const import menu, daily_budget

def main():
    planner = MenuPlanner(menu=menu, daily_budget=daily_budget)

    monthly_menu = planner.plan_monthly_menu()

    for week, dishes in enumerate(monthly_menu, 1):
        print(f'Week {week}: {dishes}')

if __name__=="__main__":
    main()

    