import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
  '''scrape information from LinkedIn profiles,
  Manually scrape information from LinkedIn profile'''

  api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
  header_dict = { 'Authorization': f'Bearer {os.environ["PROXYCURL_API_KEY"]}'}

  api_endpoint = "https://gist.githubusercontent.com/prateekchaplot/a83f61a39d0ac689499c8dd7bab66032/raw/0b9d701f3fa34bbdc0c9ae4b746d90204f3edb7c/prateek-chaplot.json"

  # requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=header_dict)
  response = requests.get(api_endpoint)

  data = response.json()
  data = {
    k: v
    for k, v in data.items()
    if v not in ([], "", "", None)
      and k not in ["people_also_viewed", "certifications"]
  }

  if data.get('groups'):
    for group_dict in data.get('groups'):
      group_dict.pop('profile_pic_url')

  return data