#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


frequencies = [135.0, 135.01, 135.02, 135.03, 135.04, 135.05, 135.06, 135.07, 135.08, 135.09, 135.1, 135.11, 135.12, 135.13, 135.14, 135.15, 135.16, 135.17, 135.18, 135.19, 135.2, 135.21, 135.22, 135.23, 135.24, 135.25, 135.26, 135.27, 135.28, 135.29, 135.3, 135.31, 135.32, 135.33, 135.34, 135.35, 135.36, 135.37, 135.38, 135.39, 135.4, 135.41, 135.42, 135.43, 135.44, 135.45, 135.46, 135.47, 135.48, 135.49, 135.5, 135.51, 135.52, 135.53, 135.54, 135.55, 135.56, 135.57, 135.58, 135.59, 135.6, 135.61, 135.62, 135.63, 135.64, 135.65, 135.66, 135.67, 135.68, 135.69, 135.7, 135.71, 135.72, 135.73, 135.74, 135.75, 135.76, 135.77, 135.78, 135.79, 135.8, 135.81, 135.82, 135.83, 135.84, 135.85, 135.86, 135.87, 135.88, 135.89, 135.9, 135.91, 135.92, 135.93, 135.94, 135.95, 135.96, 135.97, 135.98, 135.99, 136.0, 136.01, 136.02, 136.03, 136.04, 136.05, 136.06, 136.07, 136.08, 136.09, 136.1, 136.11, 136.12, 136.13, 136.14, 136.15, 136.16, 136.17, 136.18, 136.19, 136.2, 136.21, 136.22, 136.23, 136.24, 136.25, 136.26, 136.27, 136.28, 136.29, 136.3, 136.31, 136.32, 136.33, 136.34, 136.35, 136.36, 136.37, 136.38, 136.39, 136.4, 136.41, 136.42, 136.43, 136.44, 136.45, 136.46, 136.47, 136.48, 136.49, 136.5, 136.51, 136.52, 136.53, 136.54, 136.55, 136.56, 136.57, 136.58, 136.59, 136.6, 136.61, 136.62, 136.63, 136.64, 136.65, 136.66, 136.67, 136.68, 136.69, 136.7, 136.71, 136.72, 136.73, 136.74, 136.75, 136.76, 136.77, 136.78, 136.79, 136.8, 136.81, 136.82, 136.83, 136.84, 136.85, 136.86, 136.87, 136.88, 136.89, 136.9, 136.91, 136.92, 136.93, 136.94, 136.95, 136.96, 136.97, 136.98, 136.99, 137.0, 137.01, 137.02, 137.03, 137.04, 137.05, 137.06, 137.07, 137.08, 137.09, 137.1, 137.11, 137.12, 137.13, 137.14, 137.15, 137.16, 137.17, 137.18, 137.19, 137.2, 137.21, 137.22, 137.23, 137.24, 137.25, 137.26, 137.27, 137.28, 137.29, 137.3, 137.31, 137.32, 137.33, 137.34, 137.35, 137.36, 137.37, 137.38, 137.39, 137.4, 137.41, 137.42, 137.43, 137.44, 137.45, 137.46, 137.47, 137.48, 137.49, 137.5, 137.51, 137.52, 137.53, 137.54, 137.55, 137.56, 137.57, 137.58, 137.59, 137.6, 137.61, 137.62, 137.63, 137.64, 137.65, 137.66, 137.67, 137.68, 137.69, 137.7, 137.71, 137.72, 137.73, 137.74, 137.75, 137.76, 137.77, 137.78, 137.79, 137.8, 137.81, 137.82, 137.83, 137.84, 137.85, 137.86, 137.87, 137.88, 137.89, 137.9, 137.91, 137.92, 137.93, 137.94, 137.95, 137.96, 137.97, 137.98, 137.99, 138.0, 138.01, 138.02, 138.03, 138.04, 138.05, 138.06, 138.07, 138.08, 138.09, 138.1, 138.11, 138.12, 138.13, 138.14, 138.15, 138.16, 138.17, 138.18, 138.19, 138.2, 138.21, 138.22, 138.23, 138.24, 138.25, 138.26, 138.27, 138.28, 138.29, 138.3, 138.31, 138.32, 138.33, 138.34, 138.35, 138.36, 138.37, 138.38, 138.39, 138.4, 138.41, 138.42, 138.43, 138.44, 138.45, 138.46, 138.47, 138.48, 138.49, 138.5, 138.51, 138.52, 138.53, 138.54, 138.55, 138.56, 138.57, 138.58, 138.59, 138.6, 138.61, 138.62, 138.63, 138.64, 138.65, 138.66, 138.67, 138.68, 138.69, 138.7, 138.71, 138.72, 138.73, 138.74, 138.75, 138.76, 138.77, 138.78, 138.79, 138.8, 138.81, 138.82, 138.83, 138.84, 138.85, 138.86, 138.87, 138.88, 138.89, 138.9, 138.91, 138.92, 138.93, 138.94, 138.95, 138.96, 138.97, 138.98, 138.99, 139.0, 139.01, 139.02, 139.03, 139.04, 139.05, 139.06, 139.07, 139.08, 139.09, 139.1, 139.11, 139.12, 139.13, 139.14, 139.15, 139.16, 139.17, 139.18, 139.19, 139.2, 139.21, 139.22, 139.23, 139.24, 139.25, 139.26, 139.27, 139.28, 139.29, 139.3, 139.31, 139.32, 139.33, 139.34, 139.35, 139.36, 139.37, 139.38, 139.39, 139.4, 139.41, 139.42, 139.43, 139.44, 139.45, 139.46, 139.47, 139.48, 139.49, 139.5, 139.51, 139.52, 139.53, 139.54, 139.55, 139.56, 139.57, 139.58, 139.59, 139.6, 139.61, 139.62, 139.63, 139.64, 139.65, 139.66, 139.67, 139.68, 139.69, 139.7, 139.71, 139.72, 139.73, 139.74, 139.75, 139.76, 139.77, 139.78, 139.79, 139.8, 139.81, 139.82, 139.83, 139.84, 139.85, 139.86, 139.87, 139.88, 139.89, 139.9, 139.91, 139.92, 139.93, 139.94, 139.95, 139.96, 139.97, 139.98, 139.99, 140.0, 140.01, 140.02, 140.03, 140.04, 140.05, 140.06, 140.07, 140.08, 140.09, 140.1, 140.11, 140.12, 140.13, 140.14, 140.15, 140.16, 140.17, 140.18, 140.19, 140.2, 140.21, 140.22, 140.23, 140.24, 140.25, 140.26, 140.27, 140.28, 140.29, 140.3, 140.31, 140.32, 140.33, 140.34, 140.35, 140.36, 140.37, 140.38, 140.39, 140.4, 140.41, 140.42, 140.43, 140.44, 140.45, 140.46, 140.47, 140.48, 140.49, 140.5, 140.51, 140.52, 140.53, 140.54, 140.55, 140.56, 140.57, 140.58, 140.59, 140.6, 140.61, 140.62, 140.63, 140.64, 140.65, 140.66, 140.67, 140.68, 140.69, 140.7, 140.71, 140.72, 140.73, 140.74, 140.75, 140.76, 140.77, 140.78, 140.79, 140.8, 140.81, 140.82, 140.83, 140.84, 140.85, 140.86, 140.87, 140.88, 140.89, 140.9, 140.91, 140.92, 140.93, 140.94, 140.95, 140.96, 140.97, 140.98, 140.99, 141.0, 141.01, 141.02, 141.03, 141.04, 141.05, 141.06, 141.07, 141.08, 141.09, 141.1, 141.11, 141.12, 141.13, 141.14, 141.15, 141.16, 141.17, 141.18, 141.19, 141.2, 141.21, 141.22, 141.23, 141.24, 141.25, 141.26, 141.27, 141.28, 141.29, 141.3, 141.31, 141.32, 141.33, 141.34, 141.35, 141.36, 141.37, 141.38, 141.39, 141.4, 141.41, 141.42, 141.43, 141.44, 141.45, 141.46, 141.47, 141.48, 141.49, 141.5, 141.51, 141.52, 141.53, 141.54, 141.55, 141.56, 141.57, 141.58, 141.59, 141.6, 141.61, 141.62, 141.63, 141.64, 141.65, 141.66, 141.67, 141.68, 141.69, 141.7, 141.71, 141.72, 141.73, 141.74, 141.75, 141.76, 141.77, 141.78, 141.79, 141.8, 141.81, 141.82, 141.83, 141.84, 141.85, 141.86, 141.87, 141.88, 141.89, 141.9, 141.91, 141.92, 141.93, 141.94, 141.95, 141.96, 141.97, 141.98, 141.99, 142.0, 142.01, 142.02, 142.03, 142.04, 142.05, 142.06, 142.07, 142.08, 142.09, 142.1, 142.11, 142.12, 142.13, 142.14, 142.15, 142.16, 142.17, 142.18, 142.19, 142.2, 142.21, 142.22, 142.23, 142.24, 142.25, 142.26, 142.27, 142.28, 142.29, 142.3, 142.31, 142.32, 142.33, 142.34, 142.35, 142.36, 142.37, 142.38, 142.39, 142.4, 142.41, 142.42, 142.43, 142.44, 142.45, 142.46, 142.47, 142.48, 142.49, 142.5, 142.51, 142.52, 142.53, 142.54, 142.55, 142.56, 142.57, 142.58, 142.59, 142.6, 142.61, 142.62, 142.63, 142.64, 142.65, 142.66, 142.67, 142.68, 142.69, 142.7, 142.71, 142.72, 142.73, 142.74, 142.75, 142.76, 142.77, 142.78, 142.79, 142.8, 142.81, 142.82, 142.83, 142.84, 142.85, 142.86, 142.87, 142.88, 142.89, 142.9, 142.91, 142.92, 142.93, 142.94, 142.95, 142.96, 142.97, 142.98, 142.99, 143.0, 143.01, 143.02, 143.03, 143.04, 143.05, 143.06, 143.07, 143.08, 143.09, 143.1, 143.11, 143.12, 143.13, 143.14, 143.15, 143.16, 143.17, 143.18, 143.19, 143.2, 143.21, 143.22, 143.23, 143.24, 143.25, 143.26, 143.27, 143.28, 143.29, 143.3, 143.31, 143.32, 143.33, 143.34, 143.35, 143.36, 143.37, 143.38, 143.39, 143.4, 143.41, 143.42, 143.43, 143.44, 143.45, 143.46, 143.47, 143.48, 143.49, 143.5, 143.51, 143.52, 143.53, 143.54, 143.55, 143.56, 143.57, 143.58, 143.59, 143.6, 143.61, 143.62, 143.63, 143.64, 143.65, 143.66, 143.67, 143.68, 143.69, 143.7, 143.71, 143.72, 143.73, 143.74, 143.75, 143.76, 143.77, 143.78, 143.79, 143.8, 143.81, 143.82, 143.83, 143.84, 143.85, 143.86, 143.87, 143.88, 143.89, 143.9, 143.91, 143.92, 143.93, 143.94, 143.95, 143.96, 143.97, 143.98, 143.99, 144.0, 144.01, 144.02, 144.03, 144.04, 144.05, 144.06, 144.07, 144.08, 144.09, 144.1, 144.11, 144.12, 144.13, 144.14, 144.15, 144.16, 144.17, 144.18, 144.19, 144.2, 144.21, 144.22, 144.23, 144.24, 144.25, 144.26, 144.27, 144.28, 144.29, 144.3, 144.31, 144.32, 144.33, 144.34, 144.35, 144.36, 144.37, 144.38, 144.39, 144.4, 144.41, 144.42, 144.43, 144.44, 144.45, 144.46, 144.47, 144.48, 144.49, 144.5, 144.51, 144.52, 144.53, 144.54, 144.55, 144.56, 144.57, 144.58, 144.59, 144.6, 144.61, 144.62, 144.63, 144.64, 144.65, 144.66, 144.67, 144.68, 144.69, 144.7, 144.71, 144.72, 144.73, 144.74, 144.75, 144.76, 144.77, 144.78, 144.79, 144.8, 144.81, 144.82, 144.83, 144.84, 144.85, 144.86, 144.87, 144.88, 144.89, 144.9, 144.91, 144.92, 144.93, 144.94, 144.95, 144.96, 144.97, 144.98, 144.99, 145.0, 145.01, 145.02, 145.03, 145.04, 145.05, 145.06, 145.07, 145.08, 145.09, 145.1, 145.11, 145.12, 145.13, 145.14, 145.15, 145.16, 145.17, 145.18, 145.19, 145.2, 145.21, 145.22, 145.23, 145.24, 145.25, 145.26, 145.27, 145.28, 145.29, 145.3, 145.31, 145.32, 145.33, 145.34, 145.35, 145.36, 145.37, 145.38, 145.39, 145.4, 145.41, 145.42, 145.43, 145.44, 145.45, 145.46, 145.47, 145.48, 145.49, 145.5, 145.51, 145.52, 145.53, 145.54, 145.55, 145.56, 145.57, 145.58, 145.59, 145.6, 145.61, 145.62, 145.63, 145.64, 145.65, 145.66, 145.67, 145.68, 145.69, 145.7, 145.71, 145.72, 145.73, 145.74, 145.75, 145.76, 145.77, 145.78, 145.79, 145.8, 145.81, 145.82, 145.83, 145.84, 145.85, 145.86, 145.87, 145.88, 145.89, 145.9, 145.91, 145.92, 145.93, 145.94, 145.95, 145.96, 145.97, 145.98, 145.99, 146.0, 146.01, 146.02, 146.03, 146.04, 146.05, 146.06, 146.07, 146.08, 146.09, 146.1, 146.11, 146.12, 146.13, 146.14, 146.15, 146.16, 146.17, 146.18, 146.19, 146.2, 146.21, 146.22, 146.23, 146.24, 146.25, 146.26, 146.27, 146.28, 146.29, 146.3, 146.31, 146.32, 146.33, 146.34, 146.35, 146.36, 146.37, 146.38, 146.39, 146.4, 146.41, 146.42, 146.43, 146.44, 146.45, 146.46, 146.47, 146.48, 146.49, 146.5, 146.51, 146.52, 146.53, 146.54, 146.55, 146.56, 146.57, 146.58, 146.59, 146.6, 146.61, 146.62, 146.63, 146.64, 146.65, 146.66, 146.67, 146.68, 146.69, 146.7, 146.71, 146.72, 146.73, 146.74, 146.75, 146.76, 146.77, 146.78, 146.79, 146.8, 146.81, 146.82, 146.83, 146.84, 146.85, 146.86, 146.87, 146.88, 146.89, 146.9, 146.91, 146.92, 146.93, 146.94, 146.95, 146.96, 146.97, 146.98, 146.99, 147.0, 147.01, 147.02, 147.03, 147.04, 147.05, 147.06, 147.07, 147.08, 147.09, 147.1, 147.11, 147.12, 147.13, 147.14, 147.15, 147.16, 147.17, 147.18, 147.19, 147.2, 147.21, 147.22, 147.23, 147.24, 147.25, 147.26, 147.27, 147.28, 147.29, 147.3, 147.31, 147.32, 147.33, 147.34, 147.35, 147.36, 147.37, 147.38, 147.39, 147.4, 147.41, 147.42, 147.43, 147.44, 147.45, 147.46, 147.47, 147.48, 147.49, 147.5, 147.51, 147.52, 147.53, 147.54, 147.55, 147.56, 147.57, 147.58, 147.59, 147.6, 147.61, 147.62, 147.63, 147.64, 147.65, 147.66, 147.67, 147.68, 147.69, 147.7, 147.71, 147.72, 147.73, 147.74, 147.75, 147.76, 147.77, 147.78, 147.79, 147.8, 147.81, 147.82, 147.83, 147.84, 147.85, 147.86, 147.87, 147.88, 147.89, 147.9, 147.91, 147.92, 147.93, 147.94, 147.95, 147.96, 147.97, 147.98, 147.99, 148.0, 148.01, 148.02, 148.03, 148.04, 148.05, 148.06, 148.07, 148.08, 148.09, 148.1, 148.11, 148.12, 148.13, 148.14, 148.15, 148.16, 148.17, 148.18, 148.19, 148.2, 148.21, 148.22, 148.23, 148.24, 148.25, 148.26, 148.27, 148.28, 148.29, 148.3, 148.31, 148.32, 148.33, 148.34, 148.35, 148.36, 148.37, 148.38, 148.39, 148.4, 148.41, 148.42, 148.43, 148.44, 148.45, 148.46, 148.47, 148.48, 148.49, 148.5, 148.51, 148.52, 148.53, 148.54, 148.55, 148.56, 148.57, 148.58, 148.59, 148.6, 148.61, 148.62, 148.63, 148.64, 148.65, 148.66, 148.67, 148.68, 148.69, 148.7, 148.71, 148.72, 148.73, 148.74, 148.75, 148.76, 148.77, 148.78, 148.79, 148.8, 148.81, 148.82, 148.83, 148.84, 148.85, 148.86, 148.87, 148.88, 148.89, 148.9, 148.91, 148.92, 148.93, 148.94, 148.95, 148.96, 148.97, 148.98, 148.99, 149.0, 149.01, 149.02, 149.03, 149.04, 149.05, 149.06, 149.07, 149.08, 149.09, 149.1, 149.11, 149.12, 149.13, 149.14, 149.15, 149.16, 149.17, 149.18, 149.19, 149.2, 149.21, 149.22, 149.23, 149.24, 149.25, 149.26, 149.27, 149.28, 149.29, 149.3, 149.31, 149.32, 149.33, 149.34, 149.35, 149.36, 149.37, 149.38, 149.39, 149.4, 149.41, 149.42, 149.43, 149.44, 149.45, 149.46, 149.47, 149.48, 149.49, 149.5, 149.51, 149.52, 149.53, 149.54, 149.55, 149.56, 149.57, 149.58, 149.59, 149.6, 149.61, 149.62, 149.63, 149.64, 149.65, 149.66, 149.67, 149.68, 149.69, 149.7, 149.71, 149.72, 149.73, 149.74, 149.75, 149.76, 149.77, 149.78, 149.79, 149.8, 149.81, 149.82, 149.83, 149.84, 149.85, 149.86, 149.87, 149.88, 149.89, 149.9, 149.91, 149.92, 149.93, 149.94, 149.95, 149.96, 149.97, 149.98, 149.99]

swrs = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 4.04, 3.05, 3.05, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 4.04, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.06, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.03, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06, 2.06]


fig, ax = plt.subplots()
ax.plot(frequencies, swrs)

# start, end = ax.get_xlim()
starty, endy = ax.get_ylim()
# ax.xaxis.set_ticks(np.arange(start, end, 1))
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# ax.yaxis.set_ticks(np.arange(starty, endy, 0.1))
# ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

plt.show()