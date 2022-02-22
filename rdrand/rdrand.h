/* TRNG coded by Wojciech Lawren

  Copyright (C) 2021, Wojciech Lawren, All rights reserved.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
  USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
#include <stdint.h>
/* RDRAND RDSEED */
#define RC 10

#define RAND "rdrand %0\n\t"
#define SEED "rdseed %0\n\t"

#define RD(i)                                                                                                          \
    asm volatile("movl %1, %%ecx\n\t"                                                                                  \
                 "1:\n\t" i "jc 2f\n\t"                                                                                \
                 "loop 1b\n\t"                                                                                         \
                 "cmovncl %%ecx, %%eax\n\t"                                                                            \
                 "2:"                                                                                                  \
                 : "=r"(v)                                                                                             \
                 : "n"(RC)                                                                                             \
                 : "rcx", "cc")

uint64_t _rand64(void);

uint32_t _rand32(void);

uint16_t _rand16(void);

uint64_t _seed64(void);

uint32_t _seed32(void);

uint16_t _seed16(void);
