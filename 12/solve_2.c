#include <stdio.h>
#include <time.h>

int main() {

    // short int m0_posX = -1; short int m0_posY = 0; short int m0_posZ = 2; 
    // short int m1_posX = 2; short int m1_posY = -10; short int m1_posZ = -7; 
    // short int m2_posX = 4; short int m2_posY = -8; short int m2_posZ = 8; 
    // short int m3_posX = 3; short int m3_posY = 5; short int m3_posZ = -1; 

    // short int m0_posX = -8; short int m0_posY = -10; short int m0_posZ = 0; 
    // short int m1_posX = 5; short int m1_posY = 5; short int m1_posZ = 10; 
    // short int m2_posX = 2; short int m2_posY = -7; short int m2_posZ = 3; 
    // short int m3_posX = 9; short int m3_posY = -8; short int m3_posZ = -3; 

    short int m0_posX = -19; short int m0_posY = -4; short int m0_posZ = 2; 
    short int m1_posX = -9; short int m1_posY = 8; short int m1_posZ = -16; 
    short int m2_posX = -4; short int m2_posY = 5; short int m2_posZ = -11; 
    short int m3_posX = 1; short int m3_posY = 9; short int m3_posZ = -13; 


    short int m0_velX = 0; short int m0_velY = 0; short int m0_velZ = 0;
    short int m1_velX = 0; short int m1_velY = 0; short int m1_velZ = 0;
    short int m2_velX = 0; short int m2_velY = 0; short int m2_velZ = 0;
    short int m3_velX = 0; short int m3_velY = 0; short int m3_velZ = 0;

    const short int init_m0_posX = m0_posX; const short int init_m0_posY = m0_posY; const short int init_m0_posZ = m0_posZ; 
    const short int init_m1_posX = m1_posX; const short int init_m1_posY = m1_posY; const short int init_m1_posZ = m1_posZ; 
    const short int init_m2_posX = m2_posX; const short int init_m2_posY = m2_posY; const short int init_m2_posZ = m2_posZ; 
    const short int init_m3_posX = m3_posX; const short int init_m3_posY = m3_posY; const short int init_m3_posZ = m3_posZ; 

    clock_t t0 = clock();
    unsigned long long stepCount = 0;
    while(1) {
        if(m0_posX < m1_posX) { m0_velX++; } else if(m0_posX > m1_posX) { m0_velX--; }
        if(m0_posX < m2_posX) { m0_velX++; } else if(m0_posX > m2_posX) { m0_velX--; }
        if(m0_posX < m3_posX) { m0_velX++; } else if(m0_posX > m3_posX) { m0_velX--; }

        if(m0_posY < m1_posY) { m0_velY++; } else if(m0_posY > m1_posY) { m0_velY--; }
        if(m0_posY < m2_posY) { m0_velY++; } else if(m0_posY > m2_posY) { m0_velY--; }
        if(m0_posY < m3_posY) { m0_velY++; } else if(m0_posY > m3_posY) { m0_velY--; }

        if(m0_posZ < m1_posZ) { m0_velZ++; } else if(m0_posZ > m1_posZ) { m0_velZ--; }
        if(m0_posZ < m2_posZ) { m0_velZ++; } else if(m0_posZ > m2_posZ) { m0_velZ--; }
        if(m0_posZ < m3_posZ) { m0_velZ++; } else if(m0_posZ > m3_posZ) { m0_velZ--; }


        if(m1_posX < m0_posX) { m1_velX++; } else if(m1_posX > m0_posX) { m1_velX--; }
        if(m1_posX < m2_posX) { m1_velX++; } else if(m1_posX > m2_posX) { m1_velX--; }
        if(m1_posX < m3_posX) { m1_velX++; } else if(m1_posX > m3_posX) { m1_velX--; }

        if(m1_posY < m0_posY) { m1_velY++; } else if(m1_posY > m0_posY) { m1_velY--; }
        if(m1_posY < m2_posY) { m1_velY++; } else if(m1_posY > m2_posY) { m1_velY--; }
        if(m1_posY < m3_posY) { m1_velY++; } else if(m1_posY > m3_posY) { m1_velY--; }

        if(m1_posZ < m0_posZ) { m1_velZ++; } else if(m1_posZ > m0_posZ) { m1_velZ--; }
        if(m1_posZ < m2_posZ) { m1_velZ++; } else if(m1_posZ > m2_posZ) { m1_velZ--; }
        if(m1_posZ < m3_posZ) { m1_velZ++; } else if(m1_posZ > m3_posZ) { m1_velZ--; }


        if(m2_posX < m0_posX) { m2_velX++; } else if(m2_posX > m0_posX) { m2_velX--; }
        if(m2_posX < m1_posX) { m2_velX++; } else if(m2_posX > m1_posX) { m2_velX--; }
        if(m2_posX < m3_posX) { m2_velX++; } else if(m2_posX > m3_posX) { m2_velX--; }

        if(m2_posY < m0_posY) { m2_velY++; } else if(m2_posY > m0_posY) { m2_velY--; }
        if(m2_posY < m1_posY) { m2_velY++; } else if(m2_posY > m1_posY) { m2_velY--; }
        if(m2_posY < m3_posY) { m2_velY++; } else if(m2_posY > m3_posY) { m2_velY--; }

        if(m2_posZ < m0_posZ) { m2_velZ++; } else if(m2_posZ > m0_posZ) { m2_velZ--; }
        if(m2_posZ < m1_posZ) { m2_velZ++; } else if(m2_posZ > m1_posZ) { m2_velZ--; }
        if(m2_posZ < m3_posZ) { m2_velZ++; } else if(m2_posZ > m3_posZ) { m2_velZ--; }


        if(m3_posX < m0_posX) { m3_velX++; } else if(m3_posX > m0_posX) { m3_velX--; }
        if(m3_posX < m1_posX) { m3_velX++; } else if(m3_posX > m1_posX) { m3_velX--; }
        if(m3_posX < m2_posX) { m3_velX++; } else if(m3_posX > m2_posX) { m3_velX--; }

        if(m3_posY < m0_posY) { m3_velY++; } else if(m3_posY > m0_posY) { m3_velY--; }
        if(m3_posY < m1_posY) { m3_velY++; } else if(m3_posY > m1_posY) { m3_velY--; }
        if(m3_posY < m2_posY) { m3_velY++; } else if(m3_posY > m2_posY) { m3_velY--; }

        if(m3_posZ < m0_posZ) { m3_velZ++; } else if(m3_posZ > m0_posZ) { m3_velZ--; }
        if(m3_posZ < m1_posZ) { m3_velZ++; } else if(m3_posZ > m1_posZ) { m3_velZ--; }
        if(m3_posZ < m2_posZ) { m3_velZ++; } else if(m3_posZ > m2_posZ) { m3_velZ--; }
   
        m0_posX += m0_velX;
        m0_posY += m0_velY;
        m0_posZ += m0_velZ;

        m1_posX += m1_velX;
        m1_posY += m1_velY;
        m1_posZ += m1_velZ;

        m2_posX += m2_velX;
        m2_posY += m2_velY;
        m2_posZ += m2_velZ;

        m3_posX += m3_velX;
        m3_posY += m3_velY;
        m3_posZ += m3_velZ;
   
        stepCount++;
        if(stepCount % 100000000 == 0) {
            clock_t t1 = clock();
            double cpuElapsed = ((double) (t1 - t0)) / CLOCKS_PER_SEC;
            printf("Still looking at stepCount=%llu (elapsed %.2f sec)\n", stepCount, cpuElapsed);
        }

        if(m0_posX == init_m0_posX && m0_posY == init_m0_posY && m0_posZ == init_m0_posZ &&
           m1_posX == init_m1_posX && m1_posY == init_m1_posY && m1_posZ == init_m1_posZ &&
           m2_posX == init_m2_posX && m2_posY == init_m2_posY && m2_posZ == init_m2_posZ &&
           m3_posX == init_m3_posX && m3_posY == init_m3_posY && m3_posZ == init_m3_posZ && 
           m0_velX == 0 && m0_velY == 0 && m0_velZ == 0 &&
           m1_velX == 0 && m1_velY == 0 && m1_velZ == 0 &&
           m2_velX == 0 && m2_velY == 0 && m2_velZ == 0 &&
           m3_velX == 0 && m3_velY == 0 && m3_velZ == 0) {
                clock_t t1 = clock();
                double cpuElapsed = ((double) (t1 - t0)) / CLOCKS_PER_SEC;
                printf("Found repeat at stepCount=%llu (elapsed %.2f sec)\n", stepCount, cpuElapsed);
                return 0;
        }
    }
}
