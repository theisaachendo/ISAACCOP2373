import re


def extract_sentences(paragraph):
   
    # Regex pattern to match sentences ending with period, exclamation,
    # or question mark. This pattern handles sentences that may start
    # with numbers or letters
    sentence_pattern = r'(?:^|\s+)([A-Z0-9][^.!?]*[.!?])'
    
    # Find all sentences using the pattern
    sentences = re.findall(sentence_pattern, paragraph, flags=re.MULTILINE)
    
    # Clean up sentences by stripping extra whitespace
    cleaned_sentences = [sentence.strip() for sentence in sentences
                         if sentence.strip()]
    
    return cleaned_sentences


def display_sentences_and_count(sentences):
    print("\n" + "="*50)
    print("INDIVIDUAL SENTENCES FOUND:")
    print("="*50)
    
    if not sentences:
        print("No sentences found in the paragraph.")
        return 0
    
    # Display each sentence with numbering
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    
    # Display the total count
    sentence_count = len(sentences)
    print("\n" + "-"*50)
    print(f"TOTAL NUMBER OF SENTENCES: {sentence_count}")
    print("-"*50)
    
    return sentence_count


def get_user_input():
    print("="*60)
    print("SENTENCE PARSER AND COUNTER")
    print("="*60)
    print("Enter a paragraph (including sentences that may begin with "
          "numbers):")
    print("Press Enter twice when finished.\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    paragraph = " ".join(lines)
    return paragraph


def main():
    while True:
        # Get user input
        paragraph = get_user_input()
        
        if not paragraph.strip():
            print("No text entered. Please try again.")
            continue
        
        print("\nOriginal paragraph:")
        print(f'"{paragraph}"')
        
        # Extract sentences
        sentences = extract_sentences(paragraph)
        
        # Display results
        display_sentences_and_count(sentences)
        
        # Ask if user wants to continue
        print("\nWould you like to analyze another paragraph? (y/n): ", end="")
        choice = input().lower().strip()
        
        if choice != 'y' and choice != 'yes':
            print("Thank you for using the Sentence Parser!")
            break
        print()


if __name__ == "__main__":
    main()
