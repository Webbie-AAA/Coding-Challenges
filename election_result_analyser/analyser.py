def count_votes(votes: list[str]) -> dict[str, int]:
    """
    Count the votes for each candidate.

    Args:
        votes: List of candidate names (one per vote)

    Returns:
        Dictionary mapping candidate names to their vote counts
    """
    vote_name_map = {}

    for name in votes:
        if name not in vote_name_map:

            # for name in votes:
            #     vote_name_map[name] = vote_name_map.get(name, 0) + 1
            vote_name_map[name] = votes.count(name)
    return vote_name_map


def get_winner(votes: list[str]) -> str | None:
    """
    Determine the winner of the election.

    Args:
        votes: List of candidate names

    Returns:
        Winning candidate name, or None if tie or no votes
    """
    dict_of_votes = count_votes(votes)
    winners = []

    winner = max(list(dict_of_votes.values()))
    for key, value in dict_of_votes.items():
        if value == winner:
            winners.append(key)

    if len(winners) == 1:
        return winners[0]


def get_vote_percentages(votes: list[str]) -> dict[str, float]:
    """
    Calculate the percentage of votes for each candidate.

    Args:
        votes: List of candidate names

    Returns:
        Dictionary mapping candidates to their vote percentage (rounded to 2 dp)
    """
    total_count = len(votes)
    votes_dict = count_votes(votes)

    vote_percentages = {}
    for key, value in votes_dict.items():
        vote_percentages[key] = round((value/total_count)*100, 2)
    return vote_percentages


def is_majority(votes: list[str], candidate: str) -> bool:
    """
    Check if a candidate has a majority (>50%).

    Args:
        votes: List of candidate names
        candidate: Candidate to check

    Returns:
        True if candidate has more than 50% of votes
    """
    percentage_votes = get_vote_percentages(votes)

    if percentage_votes[candidate] > 50.0:
        return True
    return False
