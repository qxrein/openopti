{
  description = "OpenOpti - Dev Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            allowUnfree = true;
          };
        };

        pythonEnv = pkgs.python311.withPackages (ps: with ps; [
          python
          pip
          setuptools
          wheel
          pygobject3
        ]);
      in {
        devShells.default = pkgs.mkShell {
          packages = [
            pythonEnv

            pkgs.wrapGAppsHook

            pkgs.gtk4
            pkgs.gobject-introspection
            pkgs.gdk-pixbuf
            pkgs.pango
            pkgs.cairo
            pkgs.glib
            pkgs.gnome.gnome-themes-extra

            pkgs.vulkan-loader

            pkgs.pkg-config
            pkgs.cmake
            pkgs.meson
            pkgs.ninja
            pkgs.autoconf
            pkgs.automake
            pkgs.libtool
            pkgs.binutils
            pkgs.gcc
            pkgs.gfortran
            pkgs.swig

            pkgs.openmpi
            pkgs.hdf5
            pkgs.fftw
            pkgs.gsl
          ];

          shellHook = ''
            VENV_DIR=".venv"
            if [ ! -d "$VENV_DIR" ]; then
              echo "Creating Python venv in $VENV_DIR..."
              ${pythonEnv}/bin/python -m venv "$VENV_DIR" --system-site-packages
            fi

            . "$VENV_DIR/bin/activate"

            export GTK_PATH=$GTK_PATH:${pkgs.gnome.gnome-themes-extra}/lib/gtk-4.0
            export XDG_DATA_DIRS=$XDG_DATA_DIRS:${pkgs.gnome.gnome-themes-extra}/share:${pkgs.gtk4}/share
            export GDK_BACKEND=wayland

            echo "You are in the Nix development shell with a Python virtual environment activated."
            echo "To install simphony, meep, h5py, and empy, run:"
            echo "pip install --prefer-binary meep h5py empy simphony"
            echo "or"
            echo "pip install --prefer-binary -r requirements.txt"
          '';
        };
      }
    );
}
