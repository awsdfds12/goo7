import requests

def test_atg_world_website():
    """Tests if atg.world website is accessible."""
    url = "https://atg.world"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        print(f"Website accessible: {url} (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Website inaccessible: {url} ({e})")
        assert False 

if __name__ == "__main__":
    test_atg_world_website()
