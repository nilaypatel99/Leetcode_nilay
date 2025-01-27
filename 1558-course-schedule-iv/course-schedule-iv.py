class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # Initialize adjacency matrix to track prerequisites
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Fill direct prerequisites
        for a, b in prerequisites:
            is_prerequisite[a][b] = True

        # Apply Floyd-Warshall Algorithm to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True

        # Answer each query by checking the matrix
        result = []
        for u, v in queries:
            result.append(is_prerequisite[u][v])

        return result
