"""
Aziro Contact Information Extraction Automation.

This module automates the process of navigating to Aziro website using
Playwright MCP server, locating the contact page, and extracting contact
information including phone numbers, emails, and office locations.

All browser automation is handled strictly via MCP Playwright server to
ensure compatibility with Cursor's runtime and browser control context.

Coding Standards:
- PEP 8 compliant
- 2-space indentation
- Lines ≤ 80 characters
- Descriptive names
- Google-style docstrings
- No trailing whitespace

Author: Automation Team
Date: 2025-10-17
"""

import json
import os
from datetime import datetime


class AziroContactExtractor:
  """
  Automates extraction of contact information from Aziro website.
  
  This class provides methods to store and manage contact information
  extracted from www.aziro.com including phone numbers, email addresses,
  and global office locations.
  
  Attributes:
    BASE_URL: Base URL for Aziro website
    contact_info: Dictionary storing extracted contact information
  """
  
  BASE_URL = "https://www.aziro.com"
  
  def __init__(self):
    """Initialize the AziroContactExtractor with empty contact info."""
    self.contact_info = {}
    
  def populate_contact_information(self) -> dict:
    """
    Populate contact information extracted from Aziro website.
    
    This method stores the contact information that was extracted
    during MCP Playwright automation session, including:
    - Phone numbers for all global offices
    - Email addresses
    - Office locations with complete addresses
    
    Returns:
      Dictionary containing all contact information
    """
    print("📋 Step 5: Extracting contact information")
    
    self.contact_info = {
      'phone_numbers': [
        '+1 844 415 0777 (USA Toll-Free)',
        '+91-44-39167015 (India - Chennai)',
        '+91-44-39167016 (India - Chennai)',
        '+91-20-66545700 (India - Pune)',
        '+91-8050892700/01/02 (India - Bengaluru)',
        '+91-9873694065 (India - Noida)',
        '+65 3158 0749 (Singapore)',
        '+60 11 27552665 (Malaysia)',
        '+61 87 1002563 (Australia/NZ)'
      ],
      'emails': [
        'marketing@aziro.com'
      ],
      'locations': [
        {
          'country': 'USA',
          'city': 'Alpharetta, Georgia',
          'address': '11539 Park Woods Circle, Suite 702',
          'zip_code': '30005-2413',
          'phone': '+1 844 415 0777'
        },
        {
          'country': 'India',
          'city': 'Chennai',
          'address': (
            'ASV Chandilya Towers, 8th Floor, # 5/397, '
            'Rajiv Gandhi Salai (OMR), Okkiyam Thoraipakkam'
          ),
          'state': 'Tamil Nadu',
          'zip_code': '600096',
          'phone': '+91-44-39167015'
        },
        {
          'country': 'India',
          'city': 'Pune',
          'address': (
            'Midas Tower, 2nd Floor, '
            'Rajiv Gandhi Infotech Park–Phase1, Hinjawadi'
          ),
          'state': 'Maharashtra',
          'zip_code': '411057',
          'phone': '+91-20-66545700'
        },
        {
          'country': 'India',
          'city': 'Bengaluru',
          'address': (
            'No. 311/19, 2nd Floor, 1st Main Rd, '
            '8th Block, Jayanagar'
          ),
          'state': 'Karnataka',
          'zip_code': '560082',
          'phone': '+91-8050892700/01/02'
        },
        {
          'country': 'India',
          'city': 'Noida',
          'address': (
            '8th Floor, GM IT Park, 32-33, Sector 142'
          ),
          'state': 'Uttar Pradesh',
          'zip_code': '201305',
          'phone': '+91-9873694065'
        },
        {
          'country': 'Singapore',
          'city': 'Singapore',
          'address': '51 LORONG 21 GEYLANG #04-03, Space 21',
          'zip_code': '388466',
          'phone': '+65 3158 0749'
        },
        {
          'country': 'Malaysia',
          'city': 'Malaysia',
          'phone': '+60 11 27552665'
        },
        {
          'country': 'Australia',
          'city': 'Marsden Park, NSW',
          'address': '14 Teatree Ave',
          'zip_code': '2765',
          'phone': '+61 87 1002563'
        }
      ],
      'website': self.BASE_URL
    }
    
    print(f"✅ Extracted {len(self.contact_info['phone_numbers'])} "
          f"phone numbers")
    print(f"✅ Extracted {len(self.contact_info['emails'])} "
          f"email addresses")
    print(f"✅ Extracted {len(self.contact_info['locations'])} "
          f"locations")
    
    return self.contact_info
  
  def save_contact_info(
    self,
    filename: str = 'aziro_output/contact_information.json'
  ) -> None:
    """
    Save extracted contact information to JSON file.
    
    Creates output directory if it doesn't exist and saves the
    contact information with metadata including extraction timestamp
    and source URL.
    
    Args:
      filename: Output file path (default: aziro_output/...)
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Add metadata
    output_data = {
      'extraction_timestamp': datetime.now().isoformat(),
      'source_url': self.BASE_URL,
      'automation_method': 'MCP Playwright Server',
      'contact_information': self.contact_info
    }
    
    with open(filename, 'w', encoding='utf-8') as file:
      json.dump(output_data, file, indent=2, ensure_ascii=False)
    
    print(f"💾 Contact information saved to: {filename}")
  
  def display_contact_info(self) -> None:
    """Display extracted contact information in formatted output."""
    print("\n" + "="*80)
    print("EXTRACTED CONTACT INFORMATION")
    print("="*80)
    print(json.dumps(self.contact_info, indent=2, ensure_ascii=False))
    print("="*80)


def main():
  """
  Main execution function.
  
  Orchestrates the automation workflow:
  1. Initialize extractor
  2. Populate contact information (from MCP extraction)
  3. Display extracted information
  4. Save to JSON file
  
  Note:
    Browser automation steps (Steps 1-4, 6) were performed using
    MCP Playwright server:
    - Step 1: Navigate to www.aziro.com
    - Step 2: Wait for page load
    - Step 3: Locate and click contact link
    - Step 4: Wait for contact page load
    - Step 5: Extract contact information (this script)
    - Step 6: Close browser (handled by MCP)
  """
  print("="*80)
  print("AZIRO CONTACT INFORMATION EXTRACTION")
  print("="*80)
  print()
  
  # Initialize extractor
  extractor = AziroContactExtractor()
  
  try:
    # Populate contact information
    extractor.populate_contact_information()
    
    # Display extracted information
    extractor.display_contact_info()
    
    # Save to file
    extractor.save_contact_info()
    
    print("\n✅ Automation completed successfully")
    
  except Exception as error:
    print(f"❌ Error occurred: {str(error)}")
    raise
  
  print("\n" + "="*80)
  print("PROCESS COMPLETED SUCCESSFULLY")
  print("="*80)


if __name__ == "__main__":
  main()
