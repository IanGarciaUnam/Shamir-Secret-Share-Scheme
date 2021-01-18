from Field import Field
class LagrangeInterpolation:
    def __init__(self, prime, n, k):
        self.field = Field(prime)
        self.k = k
        self.n = n
        
    def lagrange_polynomial(self, i, x_points, x):
        """
        Reconstructs a Lagrange basis polynomial

        Args:
            i (int): [x_i]
            x_points (list): vector of x points
            x (int): value to find

        Returns:
            int: A Lagrange basis polynomial
        """
        num, dem = 1, 1 # We calculate each separately to avoid inexcat division
        for j in range(len(x_points)):
            if x_points[j] != i:
                num *= x - x_points[j] # X - x_j
                dem *= (i-x_points[j]) # x_i - x_j
                
        return self.field.division(num, dem) # (X - x_j) (x_i - x_j)^-1 -> where (x_i - x_j)^-1 is the inverse multiplicative
    
    def reconstruct_secret(self, shares, x):
        """
        Reconstructs the secret from a given list of shares

        Args:
            shares (list): share to use to reconstruct the secret
            x (int): term to find

        Raises:
            ValueError: in case that the number of shares is not enough to reconstruct the secret

        Returns:
            int: the secret
        """
        if len(shares) < self.k:
            raise ValueError("Unable to reconstruct the secret with this data")
        
        res = 0
        
        if len(shares) > self.k:
            shares = shares[:self.k]
            
        x_points, y_points = zip(*shares)
        for i in range(len(x_points)):
            poly = self.lagrange_polynomial(x_points[i], x_points, x)
            
            product = (poly * y_points[i]) % self.field.get_prime()
            
            res += product
            
        return res % self.field.get_prime()