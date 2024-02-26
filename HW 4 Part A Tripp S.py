import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


"""This program was created with the aid of chat gpt
I could not find a partner for this hw as well."""

# Define parameters
mu1, sigma1 = 0, 1
mu2, sigma2 = 175, 3

# Generate x values
x_values = np.linspace(-5, 5, 1000)
x_values_2 = np.linspace(mu2 - 10 * sigma2, mu2 + 10 * sigma2, 1000)

# Calculate PDFs
pdf1 = stats.norm.pdf(x_values, mu1, sigma1)
pdf2 = stats.norm.pdf(x_values_2, mu2, sigma2)

# Calculate CDFs
cdf1 = stats.norm.cdf(x_values, mu1, sigma1)
cdf2 = stats.norm.cdf(x_values_2, mu2, sigma2)

# Find the probabilities
# P(x < 1 | N(0,1))
prob_x_lt_1 = stats.norm.cdf(1, mu1, sigma1)
# P(x > μ + 2σ | N(175, 3))
prob_x_gt_mu_2sigma = 1 - stats.norm.cdf(mu2 + 2 * sigma2, mu2, sigma2)

# Find intersection points
intersection_x1 = 1
intersection_x2 = mu2 + 2 * sigma2
intersection_y1 = stats.norm.pdf(intersection_x1, mu1, sigma1)
intersection_y2 = stats.norm.pdf(intersection_x2, mu2, sigma2)

# Plot PDFs
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, pdf1, label='μ=0, σ=1')
plt.fill_between(x_values, pdf1, color='skyblue', alpha=0.5)
plt.scatter(intersection_x1, intersection_y1, color='red', zorder=5)
plt.axvline(x=1, color='red', linestyle='--', label='x=1')
plt.title('Probability Density Function (PDF)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.text(-4, 0.3, f'P(x<1|N(0,1)) = {prob_x_lt_1:.4f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.subplot(2, 1, 2)
plt.plot(x_values_2, pdf2, label='μ=175, σ=3')
plt.fill_between(x_values_2, pdf2, color='lightgreen', alpha=0.5)
plt.scatter(intersection_x2, intersection_y2, color='red', zorder=5)
plt.axvline(x=mu2 + 2 * sigma2, color='red', linestyle='--', label='μ + 2σ')
plt.title('Probability Density Function (PDF)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.text(150, 0.1, f'P(x>μ+2σ|N(175,3)) = {prob_x_gt_mu_2sigma:.4f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()
