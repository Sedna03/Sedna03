#!/usr/bin/env python3
"""
Aerospace Flight Calculator
A comprehensive toolkit for basic aerospace calculations useful for
drone development, RC plane design, and academic projects.

Author: GitHub Copilot for Sedna03
"""

import math


class AerodynamicsCalculator:
    """Calculate aerodynamic properties for aircraft design."""
    
    @staticmethod
    def dynamic_pressure(velocity: float, air_density: float = 1.225) -> float:
        """
        Calculate dynamic pressure (q = 0.5 * ρ * V²)
        
        Args:
            velocity: Air velocity in m/s
            air_density: Air density in kg/m³
            
        Returns:
            Dynamic pressure in Pa
        """
        return 0.5 * air_density * velocity**2
    
    @staticmethod
    def lift_force(dynamic_pressure: float, wing_area: float, lift_coefficient: float) -> float:
        """Calculate lift force (L = q * S * CL)"""
        return dynamic_pressure * wing_area * lift_coefficient
    
    @staticmethod
    def drag_force(dynamic_pressure: float, wing_area: float, drag_coefficient: float) -> float:
        """Calculate drag force (D = q * S * CD)"""
        return dynamic_pressure * wing_area * drag_coefficient


class FlightDynamicsCalculator:
    """Calculate flight dynamics and performance metrics."""
    
    @staticmethod
    def stall_speed(weight: float, wing_area: float, max_lift_coefficient: float,
                   air_density: float = 1.225) -> float:
        """Calculate stall speed (V_stall = √(2*W/(ρ*S*CL_max)))"""
        return math.sqrt(2 * weight / (air_density * wing_area * max_lift_coefficient))
    
    @staticmethod
    def turn_radius(velocity: float, bank_angle_deg: float, gravity: float = 9.81) -> float:
        """Calculate turn radius (R = V²/(g*tan(φ)))"""
        bank_angle_rad = math.radians(bank_angle_deg)
        return velocity**2 / (gravity * math.tan(bank_angle_rad))


class DroneCalculator:
    """Specialized calculations for drone/multirotor applications."""
    
    @staticmethod
    def hover_power_required(weight: float, rotor_disk_area: float,
                           air_density: float = 1.225) -> float:
        """Calculate power required for hover (ideal momentum theory)"""
        thrust = weight  # In hover, thrust equals weight
        return thrust**(3/2) / math.sqrt(2 * air_density * rotor_disk_area)
    
    @staticmethod
    def battery_flight_time(battery_capacity: float, average_current: float,
                           battery_voltage: float, discharge_efficiency: float = 0.8) -> float:
        """Estimate flight time based on battery specifications"""
        usable_capacity = battery_capacity * discharge_efficiency
        flight_time_hours = usable_capacity / average_current
        return flight_time_hours * 60  # Convert to minutes


def example_calculations():
    """Demonstrate the calculator capabilities with practical examples."""
    print("🚁 Aerospace Flight Calculator Demo 🚁")
    print("="*50)
    
    # Example 1: RC Plane Analysis
    print("\n1. RC Plane Analysis:")
    print("-" * 20)
    velocity = 15  # m/s (typical RC plane speed)
    wing_area = 0.3  # m² (typical RC plane wing area)
    weight = 20  # N (about 2kg RC plane)
    
    aero = AerodynamicsCalculator()
    dynamics = FlightDynamicsCalculator()
    
    q = aero.dynamic_pressure(velocity)
    stall_speed = dynamics.stall_speed(weight, wing_area, 1.2)  # Typical CLmax
    turn_radius = dynamics.turn_radius(velocity, 45)  # 45-degree bank
    
    print(f"Dynamic pressure: {q:.2f} Pa")
    print(f"Stall speed: {stall_speed:.2f} m/s ({stall_speed*3.6:.1f} km/h)")
    print(f"Turn radius (45° bank): {turn_radius:.1f} m")
    
    # Example 2: Drone Hover Analysis
    print("\n2. Drone Hover Analysis:")
    print("-" * 22)
    
    drone_calc = DroneCalculator()
    drone_weight = 25  # N (about 2.5kg drone)
    rotor_area = 0.2  # m² (total disk area for all rotors)
    battery_cap = 5.0  # Ah
    battery_voltage = 14.8  # V (4S LiPo)
    
    hover_power = drone_calc.hover_power_required(drone_weight, rotor_area)
    hover_current = hover_power / battery_voltage
    flight_time = drone_calc.battery_flight_time(battery_cap, hover_current, battery_voltage)
    
    print(f"Hover power required: {hover_power:.1f} W")
    print(f"Hover current draw: {hover_current:.1f} A")
    print(f"Estimated hover time: {flight_time:.1f} minutes")


if __name__ == "__main__":
    example_calculations()