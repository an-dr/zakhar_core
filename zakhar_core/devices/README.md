# devices package

Each device has a following structure:

```none
.
└── device - module representing the device
    ├── constants relevant for the device
    │   ├── [ADDR_DEVICE]
    │   ├── [CMD_DEVICE]
    │   └── [...]
    └── dev - instance of the device
        ├── [methods]
        └── stop() - each device should support this method
```
