class Clout(object):
    """
    Clout measures the "influence" score for a set of people, based on the 
    score of the followers of the person. That is, a person's score is
    the sum of its followers' scores, where each score point equals a follower.
    That means that a followee accumulates both the follower and his network
    of followers.
    """
    def __init__(self):
        self.people = []

    def get_person_by_name(self, name):
        """
        Get person from set of people by name string, creating one if it 
        doesn't exist, and add to existing set of people.
        :param string: name:
        :return obj: person:
        """
        # If person already exists, return him/her.
        for person in self.people:
            if person.name == name:
                return person

        # No person exists with that name, create one and add to people list.
        new_person = Person(name=name)
        self.people.append(new_person)

        return new_person

    def follow(self, follower_name, followee_name):
        """
        Set the current followee for a follower and adjust scores accordingly.

        A person can have an unlimited number of followers.
        A person can only follow one person.
        A person can change who they follow.
        A person may not follow her/himself.

        :param follower:
        :param followee:
        :return bool:
        """
        follower = self.get_person_by_name(follower_name)
        followee = self.get_person_by_name(followee_name)

        if follower == followee:
            # Don't allow follower to follow himself.
            return False

        # Unset current_followee score: current_followee score = current_followee score - (follower + follower score)
        if follower.current_followee:
            follower.current_followee.add_to_score(-(1 + follower.score))
    
        # Adjust followee current_followee score: followee.current_followee score = followee.current_followee score + follower + follower score
        if followee.current_followee:
            followee.current_followee.add_to_score(1 + follower.score)

        # Set followee score: followee score = followee score + follower + follower score
        followee.add_to_score(1 + follower.score)

        # Finally, set follower's current_followee to followee
        follower.set_current_followee(followee)

        # Reorder set of people in score descending order.
        self.people.sort(key=lambda person: person.score, reverse=True)

        return True

    def clout(self, name=None):
        """
        If person provided, print the clout of the person. Otherwise print the
        clout of all the people, in score descending order.
        :return string:
        """
        # TODO: Separate out the string printing from the functionality.
        clout = ""

        if name:
            person = self.get_person_by_name(name)
            clout = "{0} has {1} follower(s).\n".format(person.name, person.score)
        else:
            for person in self.people:
                clout += "{0} has {1} follower(s).\n".format(person.name, person.score)

        return clout


class Person(object):
    # TODO: Add docstrings
    # TODO: Add value checking

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.current_followee = None
        self.followers = []
        self.score = 0

    def set_current_followee(self, followee):
        self.current_followee = followee

    def add_follower(self, follower):
        self.followers.append(follower)

    def add_to_score(self, score):
        self.score += score
