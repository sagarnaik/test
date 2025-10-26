#!/usr/bin/env python3
"""
Aziro.com Contact Information Extraction Automation Script.

This module implements web automation using Playwright to extract contact
information from aziro.com following a structured 6-step workflow with
proper error handling and PEP 8 compliance.

Author: Automation Engineer
Date: 2025-10-26
"""

import time
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
from playwright.sync_api import sync_playwright, Page, Browser


class AziroContactExtractor:
  """
  Aziro.com contact information extraction automation class.
  
  This class implements the complete automation workflow for extracting
  contact information from aziro.com using Playwright with proper error
  handling and logging.
  """
  
  # Class-level constants
  BASE_URL = "https://www.aziro.com"
  CONTACT_URL = "https://www.aziro.com/contact-us/"
  OUTPUT_DIR = Path("aziro_output")
  TIMEOUT_MS = 30000
  WAIT_DELAY = 2
  
  def __init__(self) -> None:
    """Initialize the AziroContactExtractor with default settings."""
    self.OUTPUT_DIR.mkdir(exist_ok=True)
    self.session_data = self._initialize_session_data()
    self.contact_info = {}
  
  def _initialize_session_data(self) -> Dict:
    """
    Initialize session data structure for tracking automation progress.
    
    Returns:
        Dict: Initialized session data dictionary.
    """
    return {
      "timestamp": datetime.now().isoformat(),
      "base_url": self.BASE_URL,
      "contact_url": self.CONTACT_URL,
      "steps_completed": [],
      "contact_info": {},
      "errors": [],
      "notes": []
    }
  
  def log_step(
    self,
    step_name: str,
    status: str = "completed",
    details: Optional[Dict] = None
  ) -> None:
    """
    Log step completion for tracking and debugging.
    
    Args:
        step_name: Name of the automation step.
        status: Status of the step (completed/failed).
        details: Additional details about the step execution.
    """
    step_log = {
      "step": step_name,
      "status": status,
      "timestamp": datetime.now().isoformat(),
      "details": details or {}
    }
    self.session_data["steps_completed"].append(step_log)
    print(f"✓ {step_name}: {status}")
  
  def navigate_to_homepage(self, page: Page) -> bool:
    """
    Step 1: Navigate to Aziro.com homepage.
    
    Args:
        page: Playwright page instance.
    
    Returns:
        bool: True if navigation successful, False otherwise.
    """
    try:
      print("🚀 Step 1: Navigating to aziro.com...")
      
      page.goto(self.BASE_URL, wait_until="domcontentloaded")
      page.wait_for_load_state("networkidle")
      
      print(f"📍 Current URL: {page.url}")
      
      self.log_step("Navigate to homepage", "completed", {
        "url": page.url
      })
      return True
      
    except Exception as error:
      error_msg = f"Failed to navigate: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Navigate to homepage", "failed", {
        "error": str(error)
      })
      return False
  
  def wait_for_page_load(self, page: Page) -> bool:
    """
    Step 2: Wait for homepage to fully load and verify content.
    
    Args:
        page: Playwright page instance.
    
    Returns:
        bool: True if page loaded successfully, False otherwise.
    """
    try:
      print("⏳ Step 2: Waiting for homepage to fully load...")
      
      time.sleep(self.WAIT_DELAY)
      page_title = page.title()
      
      print(f"✅ Page loaded: {page_title}")
      
      self.log_step("Wait for page load", "completed", {
        "title": page_title
      })
      return True
      
    except Exception as error:
      error_msg = f"Failed to verify page load: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Wait for page load", "failed", {
        "error": str(error)
      })
      return False
  
  def locate_and_click_contact_link(self, page: Page) -> bool:
    """
    Step 3: Locate and click the Contact link or button.
    
    Args:
        page: Playwright page instance.
    
    Returns:
        bool: True if contact link found/clicked, False otherwise.
    """
    try:
      print("🔍 Step 3: Locating and clicking Contact link...")
      
      # Try multiple selectors for contact link
      contact_selectors = [
        "a[href*='contact']",
        "a:has-text('Contact')",
        "a:has-text('Contact Us')",
        ".contact-link"
      ]
      
      clicked = False
      for selector in contact_selectors:
        try:
          element = page.locator(selector).first
          if element.is_visible(timeout=5000):
            element.click()
            clicked = True
            print(f"✅ Clicked contact link: {selector}")
            break
        except Exception:
          continue
      
      if not clicked:
        # Direct navigation as fallback
        print("📍 Direct navigation to contact page")
        page.goto(self.CONTACT_URL, wait_until="domcontentloaded")
      
      self.log_step("Locate and click contact link", "completed", {
        "method": "click" if clicked else "direct_navigation"
      })
      return True
      
    except Exception as error:
      error_msg = f"Failed to find/click contact link: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Locate and click contact link", "failed", {
        "error": str(error)
      })
      return False
  
  def wait_for_contact_page_load(self, page: Page) -> bool:
    """
    Step 4: Wait for Contact page to load completely.
    
    Args:
        page: Playwright page instance.
    
    Returns:
        bool: True if contact page loaded, False otherwise.
    """
    try:
      print("⏳ Step 4: Waiting for Contact page to load...")
      
      page.wait_for_load_state("networkidle")
      time.sleep(self.WAIT_DELAY)
      
      print(f"📍 Current URL: {page.url}")
      
      self.log_step("Wait for contact page load", "completed", {
        "url": page.url
      })
      return True
      
    except Exception as error:
      error_msg = f"Failed to verify contact page load: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Wait for contact page load", "failed", {
        "error": str(error)
      })
      return False
  
  def extract_contact_information(self, page: Page) -> bool:
    """
    Step 5: Extract Contact Information from the page.
    
    Args:
        page: Playwright page instance.
    
    Returns:
        bool: True if contact info extracted, False otherwise.
    """
    try:
      print("📋 Step 5: Extracting Contact Information...")
      
      # Get page content
      content = page.content()
      visible_text = page.locator('body').text_content()
      
      # Extract information (basic extraction)
      self.contact_info = {
        "company_name": "Aziro",
        "website": self.BASE_URL,
        "contact_page": page.url,
        "extraction_timestamp": datetime.now().isoformat(),
        "page_title": page.title(),
        "content_preview": visible_text[:500] if visible_text else ""
      }
      
      # Try to find specific contact elements
      contact_patterns = {
        "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "phone": r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
      }
      
      import re
      for key, pattern in contact_patterns.items():
        matches = re.findall(pattern, content)
        if matches:
          self.contact_info[key] = matches[0]
      
      self.session_data["contact_info"] = self.contact_info
      
      print("\n📊 Extracted Contact Information:")
      for key, value in self.contact_info.items():
        if key != "content_preview":
          print(f"   {key}: {value}")
      
      # Save to file
      contact_file = self.OUTPUT_DIR / "contact_information.json"
      with open(contact_file, 'w') as f:
        json.dump(self.contact_info, f, indent=2)
      
      print(f"\n📄 Contact info saved to: {contact_file}")
      
      self.log_step("Extract contact information", "completed", {
        "fields_extracted": list(self.contact_info.keys())
      })
      return True
      
    except Exception as error:
      error_msg = f"Failed to extract contact info: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Extract contact information", "failed", {
        "error": str(error)
      })
      return False
  
  def close_browser(self, browser: Browser) -> bool:
    """
    Step 6: Close browser gracefully.
    
    Args:
        browser: Playwright browser instance.
    
    Returns:
        bool: True if browser closed successfully, False otherwise.
    """
    try:
      print("🔒 Step 6: Closing browser gracefully...")
      
      browser.close()
      
      self.log_step("Close browser gracefully", "completed")
      return True
      
    except Exception as error:
      error_msg = f"Failed to close browser: {str(error)}"
      self.session_data["errors"].append(error_msg)
      self.log_step("Close browser gracefully", "failed", {
        "error": str(error)
      })
      return False
  
  def save_session_report(self) -> Optional[Path]:
    """
    Save complete session report to JSON file.
    
    Returns:
        Optional[Path]: Path to saved report file, None if failed.
    """
    try:
      timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
      report_filename = f"session_report_{timestamp}.json"
      report_file = self.OUTPUT_DIR / report_filename
      
      with open(report_file, 'w') as f:
        json.dump(self.session_data, f, indent=2)
      
      print(f"\n📊 Session report saved to: {report_file}")
      return report_file
      
    except Exception as error:
      print(f"❌ Failed to save session report: {str(error)}")
      return None
  
  def run_automation(self) -> bool:
    """
    Run the complete 6-step automation workflow.
    
    Returns:
        bool: True if all steps successful, False otherwise.
    """
    print("🤖 Starting Aziro.com Contact Information Extraction")
    print("=" * 70)
    
    with sync_playwright() as playwright:
      browser = playwright.chromium.launch(headless=False)
      context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
      )
      page = context.new_page()
      page.set_default_timeout(self.TIMEOUT_MS)
      
      try:
        # Execute all automation steps
        steps = [
          lambda: self.navigate_to_homepage(page),
          lambda: self.wait_for_page_load(page),
          lambda: self.locate_and_click_contact_link(page),
          lambda: self.wait_for_contact_page_load(page),
          lambda: self.extract_contact_information(page),
          lambda: self.close_browser(browser)
        ]
        
        success_count = 0
        for step_func in steps:
          if step_func():
            success_count += 1
          else:
            print("⚠️  Step failed, but continuing...")
        
        # Generate final report
        print("\n" + "=" * 70)
        print(f"🎯 Automation completed: {success_count}/{len(steps)} "
              f"steps successful")
        
        if self.session_data["errors"]:
          print(f"❌ Errors: {len(self.session_data['errors'])}")
          for error in self.session_data["errors"]:
            print(f"   • {error}")
        
        # Save session report
        self.save_session_report()
        
        print("\n✅ Automation workflow finished!")
        return success_count == len(steps)
        
      except Exception as error:
        print(f"\n💥 Unexpected error: {str(error)}")
        return False


def main() -> None:
  """Main function to execute the Aziro automation workflow."""
  try:
    extractor = AziroContactExtractor()
    success = extractor.run_automation()
    
    if success:
      print("\n🎉 All steps completed successfully!")
      print("📁 Check the 'aziro_output' directory for results")
    else:
      print("\n⚠️  Some steps failed. Check session report for details")
    
  except KeyboardInterrupt:
    print("\n\n⏹️  Automation interrupted by user")
  except Exception as error:
    print(f"\n💥 Unexpected error: {str(error)}")


if __name__ == "__main__":
  main()
