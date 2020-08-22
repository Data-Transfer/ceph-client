#!/bin/env python
from astropy.io import fits
import sys
import json


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Extract HDUs boundaries as Ceph metadata and stores them in file <ceph bucket>-bounds")
        print(f"usage: {sys.argv[0]} <id_data_device.fits file> <ceph bucket>",
              file=sys.stderr)
        sys.exit(1)
    fits_file = sys.argv[1]
    field_separator = '_'
    id, date, device = fits_file.split(field_separator)[:3]
    assert device  # check that there are indeed three fields
    hdus = fits.open(fits_file)
    header_info = []
    for hdu in hdus:
        fi = hdu.fileinfo()
        hdr_start,  data_start, data_size = \
            fi['hdrLoc'], fi['datLoc'], fi['datSpan']
        header_info.append({"hdrLoc": hdr_start,
                            "datLoc": data_start,
                            "datSpan": data_size})
    json_headers = {"hdu_boundaries": header_info}
    meta_file = fits_file + ".bounds"
    ceph_bucket = sys.argv[2] + "-bounds"
    meta = {"x-amz-meta-id": id,
            "x-amz-meta-date": date,
            "x-amz-meta-device": device,
            "x-amz-meta-bounds": meta_file,
            "x-amz-meta-bounds-bucket": ceph_bucket}
    with open(meta_file, "wb") as f:
        f.write(bytes(json.dumps(json_headers), "utf-8"))        
    for k, v in meta.items():
        print(f"{k}:{v}", end=';')
    print()