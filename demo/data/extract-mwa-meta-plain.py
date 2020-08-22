#!/bin/env python
from astropy.io import fits
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Insert header loacations in ceph metadata")
        print(f"usage: {sys.argv[0]} <id_data_device.fits file>",
              file=sys.stderr)
        sys.exit(1)
    fits_file = sys.argv[1]
    fname = os.path.basename(fits_file)
    field_separator = '_'
    id, date, device = fname.split(field_separator)[:3]
    assert device  # check that there are indeed three fields
    hdus = fits.open(fits_file)
    boundary_list = [str(h.fileinfo()['hdrLoc']) for h in hdus]
    meta = {"x-amz-meta-id": id,
            "x-amz-meta-date": date,
            "x-amz-meta-device": device,
            "x-amz-meta-bounds": ",".join(boundary_list)}
    meta_list = [f"{k}:{v}" for k, v in meta.items()]
    print(";".join(meta_list))
