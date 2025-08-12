import sys
from .app import OpenOptiApplication

def main():
    """Main function to run the application."""
    app = OpenOptiApplication()
    return app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main())
