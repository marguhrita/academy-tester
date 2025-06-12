try:
    import academy_tester
    print("Import successful!")
except ImportError as e:
    print(f"ImportError caught: {e}")
except Exception as e: # Catch any other unexpected errors during import
        print(f"Other Exception caught during import: {e}")
