If trying bufferoverflow on Kali PC, disable ASLR and allow Ptrace

Disable ASLR
sudo sysctl -w kernel.randomize_va_space=0

Allow Ptrace
sudo sysctl -w kernel.yama.ptrace_scope=0
