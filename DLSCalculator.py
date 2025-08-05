RESOURCE_TABLE = {
    0:  [100, 93, 85, 74, 66, 56, 45, 34, 24, 14, 5],
    5:  [96, 90, 82, 71, 62, 51, 41, 30, 20, 10, 4],
    10: [92, 86, 78, 67, 58, 48, 37, 27, 17, 8, 3],
    15: [88, 82, 74, 63, 54, 44, 33, 23, 13, 7, 3],
    20: [84, 78, 70, 59, 49, 39, 29, 19, 11, 6, 3],
    25: [79, 74, 66, 55, 45, 35, 25, 16, 9, 5, 2],
    30: [74, 69, 61, 50, 40, 30, 21, 13, 8, 4, 2],
    35: [68, 64, 56, 45, 35, 26, 18, 11, 6, 3, 2],
    40: [62, 58, 50, 39, 30, 22, 15, 9, 5, 3, 1],
    45: [55, 52, 44, 34, 26, 19, 13, 8, 4, 2, 1],
    50: [100, 95, 88, 78, 68, 57, 45, 34, 24, 14, 5],
}
def get_resource(overs_left, wickets_lost):
    overs = round(overs_left / 5) * 5
    overs = min(max(overs, 0), 50)
    wickets = min(max(wickets_lost, 0), 10)
    return RESOURCE_TABLE.get(overs, RESOURCE_TABLE[0])[wickets]
def calculate_dls_target(
    total_overs_or_balls: int,
    team1_score: int,
    balls_elapsed_2nd: int,
    wickets_lost_2nd: int,
    reduced_balls_2nd: int
):
    if total_overs_or_balls == 20:
        match_type = "T20"
        total_balls = 120
        min_balls_required = 30
    elif total_overs_or_balls == 50:
        match_type = "ODI"
        total_balls = 300
        min_balls_required = 120
    elif total_overs_or_balls == 100:
        match_type = "Hundred"
        total_balls = 100
        min_balls_required = 25
    else:
        return "Unsupported match type. Only 20, 50 overs or 100-ball matches are supported."
    if balls_elapsed_2nd < min_balls_required:
        return f"DLS method cannot be applied. At least {min_balls_required} balls must be bowled in the 2nd innings of a {match_type} match."
    overs_first = total_balls / 6
    overs_elapsed_2nd = balls_elapsed_2nd / 6
    overs_reduced_2nd = reduced_balls_2nd / 6
    overs_left_2nd = overs_reduced_2nd - overs_elapsed_2nd
    res1 = get_resource(overs_first, 0)
    res2 = get_resource(overs_left_2nd, wickets_lost_2nd)
    print(f"Match Type: {match_type}")
    print(f"Resource - 1st innings: {res1}%")
    print(f"Resource - 2nd innings: {res2}%")
    par_score = int(team1_score * res2 / res1)
    return f"DLS Target for Team 2: {par_score + 1}"
if __name__ == "__main__":
    match_format = int(input("Enter match format (20 for T20(I), 50 for ODI, 100 for The Hundred): "))
    team1_score = int(input("Enter 1st innings team total: "))
    balls_elapsed = int(input("Enter balls elapsed in 2nd innings: "))
    wickets_lost = int(input("Enter number of wickets lost in 2nd innings: "))
    reduced_balls = int(input("Enter reduced number of balls in 2nd innings: "))
    result = calculate_dls_target(
        match_format, team1_score, balls_elapsed, wickets_lost, reduced_balls
    )
    print("\n" + result)
