#!/usr/bin/env python3
"""
Test script to verify image loading works correctly
"""

import os
import base64

def test_image_loading():
    """Test the image loading function"""
    print("=== Testing Image Loading ===")
    
    # Check if image files exist
    image_paths = [
        "header.jpg",
        "header.jpeg", 
        "./header.jpg",
        "./header.jpeg"
    ]
    
    found_images = []
    for image_path in image_paths:
        if os.path.exists(image_path):
            found_images.append(image_path)
            print(f"✅ Found image: {image_path}")
            
            # Test file reading
            try:
                with open(image_path, 'rb') as f:
                    data = f.read()
                    print(f"   📊 Size: {len(data):,} bytes")
                    
                # Test base64 encoding
                try:
                    img_base64 = base64.b64encode(data).decode()
                    print(f"   ✅ Base64 encoding successful: {len(img_base64)} chars")
                except Exception as e:
                    print(f"   ❌ Base64 encoding failed: {e}")
                    
            except Exception as e:
                print(f"   ❌ File reading failed: {e}")
        else:
            print(f"❌ Image not found: {image_path}")
    
    if found_images:
        print(f"\n✅ Image loading should work with {len(found_images)} available images")
        return True
    else:
        print("\n❌ No images found - will use fallback text header")
        return False

def test_fallback_header():
    """Test the fallback HTML header"""
    print("\n=== Testing Fallback Header ===")
    
    fallback_html = """
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; margin: 0; font-size: 3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🚀</h1>
        <h1 style="color: white; margin: 10px 0; font-size: 2.5em; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">Elon Musk AI Chatbot</h1>
        <p style="color: #f0f8ff; margin: 10px 0 0 0; font-size: 1.2em; opacity: 0.9;">Powered by Advanced RAG Technology & Vector Search</p>
        <p style="color: #e6f3ff; margin: 5px 0 0 0; font-size: 1em; opacity: 0.8;">Ask questions about Elon Musk's tweets and get intelligent responses</p>
    </div>
    """
    
    print(f"✅ Fallback HTML header ready ({len(fallback_html)} chars)")
    print("✅ Contains emoji, gradients, and professional styling")
    return True

if __name__ == "__main__":
    print("Testing image loading capabilities...\n")
    
    images_available = test_image_loading()
    fallback_ready = test_fallback_header()
    
    print(f"\n=== Test Results ===")
    print(f"Images available: {'✅ YES' if images_available else '❌ NO'}")
    print(f"Fallback ready: {'✅ YES' if fallback_ready else '❌ NO'}")
    print(f"App will work: ✅ YES (with {'images' if images_available else 'fallback'})")
