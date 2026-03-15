#!/usr/bin/env python3
"""
Simple test script to demonstrate the ROM Library API functionality.
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    """Test all API endpoints."""
    print("🧪 Testing ROM Library API")
    print("=" * 50)

    try:
        # Test root endpoint
        print("📍 Testing root endpoint...")
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint: {data['message']} v{data['version']}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return

        # Test systems endpoint
        print("\n📍 Testing /systems endpoint...")
        response = requests.get(f"{BASE_URL}/systems")
        if response.status_code == 200:
            systems = response.json()
            print(f"✅ Retrieved {len(systems)} systems")
            print("📋 First 3 systems:")
            for system in systems[:3]:
                print(f"   • {system['system']}: {system['system_name']}")
        else:
            print(f"❌ Systems endpoint failed: {response.status_code}")
            return

        # Test search endpoint
        print("\n📍 Testing /systems/search endpoint...")
        response = requests.get(f"{BASE_URL}/systems/search?q=Nintendo&limit=5")
        if response.status_code == 200:
            results = response.json()
            print(f"✅ Search for 'Nintendo' returned {len(results)} results")
            for result in results:
                print(f"   • {result['system']}: {result['system_name']}")
        else:
            print(f"❌ Search endpoint failed: {response.status_code}")
            return

        # Test individual system endpoint
        print("\n📍 Testing /systems/{id} endpoint...")
        response = requests.get(f"{BASE_URL}/systems/nes")
        if response.status_code == 200:
            system = response.json()
            print(f"✅ Retrieved NES: {system['system_name']}")
        else:
            print(f"❌ Individual system endpoint failed: {response.status_code}")

        # Test 404 error
        print("\n📍 Testing 404 error handling...")
        response = requests.get(f"{BASE_URL}/systems/nonexistent")
        if response.status_code == 404:
            print("✅ 404 error handled correctly")
        else:
            print(f"❌ Expected 404, got {response.status_code}")

        print("\n🎉 All API tests completed successfully!")
        print(f"\n📖 API Documentation:")
        print(f"   Swagger UI: {BASE_URL}/docs")
        print(f"   ReDoc: {BASE_URL}/redoc")

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API server. Is it running?")
        print("   Start it with: python run_api.py")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    test_api()