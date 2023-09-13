#include <time.h>

/**
 * Get local time and return it in the format "HH:MM:SS".
 */
char* get_current_time() {

    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    
    char* timeStr = (char*)malloc(9 * sizeof(char));
    if (timeStr != NULL) {
        strftime(timeStr, 9, "%H:%M:%S", timeinfo);
    }
    
    return timeStr;
}
