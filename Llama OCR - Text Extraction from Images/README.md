# Llama OCR - Text Extraction from Images 🦙

[![Watch the video](https://img.youtube.com/vi/fFG8rYKWXpk/maxresdefault.jpg)](https://youtu.be/fFG8rYKWXpk)

## Project Overview
Llama OCR is a sophisticated web application that leverages Llama 3.2 Vision AI to extract and structure text content from images. The application transforms complex image-based text into well-organized, readable Markdown format, making it ideal for document digitization and text extraction tasks.

## What Makes This Project Special
The application excels at:
- Converting image-based text into structured digital content
- Maintaining original text formatting and hierarchy
- Organizing extracted content in a clear, readable format
- Providing instant text extraction with minimal user interaction

## Core Functionality

### 1. Image Processing
The application handles images through these steps:
- Accepts multiple image formats (PNG, JPEG, JPG)
- Converts uploaded images to base64 encoding
- Processes images through Llama 3.2 Vision AI

### 2. Text Extraction
For each analyzed image, the system:
- Identifies all text elements within the image
- Recognizes different text hierarchies (headings, paragraphs, lists)
- Maintains original formatting structure
- Converts content into well-organized Markdown

### 3. Content Organization
The AI structures the extracted text by:
- Identifying and preserving headings and subheadings
- Recognizing and formatting bullet points and numbered lists
- Maintaining special formatting (bold, italic, etc.)
- Creating appropriate code blocks for technical content

### 4. User Interface
Built with Streamlit, the interface features:
- A clean, two-column layout
- Simple image upload functionality
- Clear presentation of extracted text
- One-click content clearing
- Sidebar image preview

## Project Benefits
- **Efficient Text Extraction**: Convert image-based text to digital format instantly
- **Structured Output**: Get well-organized, formatted text in Markdown
- **Format Preservation**: Maintain original document structure and formatting
- **User-Friendly**: Simple interface requiring minimal user input
- **Quick Processing**: Real-time text extraction and formatting

## Future Enhancements
The project architecture supports future additions such as:
- Batch processing of multiple images
- Additional output format options
- Custom formatting templates
- Text editing capabilities
- Export functionality
- OCR language support expansion
