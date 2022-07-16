class FriendsUC3M:
    def __init__(self):
        self.users = {}

    def addUser(self,email):
        if email in self.users:
            print(email, 'already exists!!!')
            return
        self.users[email] = []

    def getFriends(self,email):
        if email not in self.users:
            print(email, 'does not exist!!!')
            return
        return self.users[email]

    def areFriends(self,email1,email2):
        if email1 not in self.users:
            return False
        if email2 not in self.users:
            return False
        if email2 in self.users[email1]:
            return True
        if email1 in self.users[email2]:
            return True
        return False

    def addFriends(self,email1,email2):
        if email1 not in self.users:
            self.addUser(email1)
        if email2 not in self.users:
            self.addUser(email2)
        if not self.areFriends(email1,email2):
            self.users[email1].append(email2)
            self.users[email2].append(email1)

    def friendsAtdistance(self, email, k):
        visited = {}
        distance = {}

        for i in self.users.keys():
            visited[i] = False
            distance[i] = 0

        queue = []
        queue.append(email)
        distance[email] = 0
        visited[email] = True
        l_friends = []

        while queue and l_friends is None:
            s = queue.pop(0)  # Pop queue's first element and look for its adjacent vertices
            for friend in self.users[s]:
                if visited[friend] == False:
                    queue.append(friend)  # append vertex's adjacent vertex if not visited
                    visited[friend] = True  # The vertex won't be visited again
                    distance[friend] = distance[s] + 1
                    if distance[friend] == k:
                        l_friends.append(friend)
        return l_friends



    