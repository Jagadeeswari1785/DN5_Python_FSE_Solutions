{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a62d49fcd0830173dea7327'),
    '1': ObjectId('6a62d49fcd0830173dea7328'),
    '2': ObjectId('6a62d49fcd0830173dea7329'),
    '3': ObjectId('6a62d49fcd0830173dea732a'),
    '4': ObjectId('6a62d49fcd0830173dea732b'),
    '5': ObjectId('6a62d49fcd0830173dea732c'),
    '6': ObjectId('6a62d49fcd0830173dea732d'),
    '7': ObjectId('6a62d49fcd0830173dea732e'),
    '8': ObjectId('6a62d49fcd0830173dea732f'),
    '9': ObjectId('6a62d49fcd0830173dea7330')
  }
}

{
  _id: ObjectId('6a62d49fcd0830173dea7327'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching.',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a62d49fcd0830173dea732b'),
  student_id: 5,
  course_code: 'CS102',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Loved it.',
  tags: [
    'good-examples',
    'interesting'
  ],
  submitted_at: 2022-11-15T10:00:00.000Z,
  attachments: [
    {
      filename: 'project.pdf',
      size_kb: 200
    }
  ]
}

{
  _id: ObjectId('6a62d49fcd0830173dea732e'),
  student_id: 8,
  course_code: 'CS105',
  semester: '2021-EVEN',
  rating: 5,
  comments: 'Excellent.',
  tags: [
    'good-examples'
  ],
  submitted_at: 2021-12-01T10:00:00.000Z,
  attachments: [
    {
      filename: 'exam.pdf',
      size_kb: 160
    }
  ]
}

{
  _id: ObjectId('6a62d49fcd0830173dea7327'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching.',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}

{
  _id: ObjectId('6a62d49fcd0830173dea7328'),
  student_id: 2,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 4,
  comments: 'Good course.',
  tags: [
    'challenging',
    'interesting'
  ],
  submitted_at: 2022-11-25T09:00:00.000Z,
  attachments: [
    {
      filename: 'assignment.pdf',
      size_kb: 180
    }
  ]
}

{
  _id: ObjectId('6a62d49fcd0830173dea7329'),
  student_id: 3,
  course_code: 'CS101',
  semester: '2021-EVEN',
  rating: 2,
  comments: 'Too difficult.',
  tags: [
    'challenging'
  ],
  submitted_at: 2021-12-10T08:00:00.000Z,
  attachments: [
    {
      filename: 'feedback.pdf',
      size_kb: 120
    }
  ]
}

{
  student_id: 1,
  course_code: 'CS101',
  rating: 5
}

{
  student_id: 2,
  course_code: 'CS101',
  rating: 4
}
{
  student_id: 3,
  course_code: 'CS101',
  rating: 2
}
{
  student_id: 4,
  course_code: 'CS102',
  rating: 3
}

{
  student_id: 5,
  course_code: 'CS102',
  rating: 5
}
{
  student_id: 6,
  course_code: 'CS103',
  rating: 1
}
{
  student_id: 7,
  course_code: 'CS104',
  rating: 4
}
{
  student_id: 8,
  course_code: 'CS105',
  rating: 5
}
{
  student_id: 9,
  course_code: 'CS106',
  rating: 3
}
{
  student_id: 10,
  course_code: 'CS107',
  rating: 4
}

db.feedback.updateMany(
  { rating: { $lt: 3 } },
  {
    $set: {
      needs_review: true
    }
  }
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
db.feedback.updateMany(
  { needs_review: true },
  {
    $push: {
      tags: "reviewed"
    }
  }
)

{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}





{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'college_nosql.feedback',
    parsedQuery: {
      course_code: {
        '$eq': 'CS101'
      }
    },
    indexFilterSet: false,
    queryHash: '83CE04A5',
    planCacheShapeHash: '83CE04A5',
    planCacheKey: 'E4E1D11D',
    optimizationTimeMillis: 4,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'FETCH',
      nss: 'college_nosql.feedback',
      inputStage: {
        stage: 'IXSCAN',
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 2,
    executionTimeMillis: 37,
    totalKeysExamined: 2,
    totalDocsExamined: 2,
    executionStages: {
      isCached: false,
      stage: 'FETCH',
      nReturned: 2,
      executionTimeMillisEstimate: 31,
      works: 3,
      advanced: 2,
      needTime: 0,
      needYield: 0,
      saveState: 1,
      restoreState: 1,
      isEOF: 1,
      nss: 'college_nosql.feedback',
      docsExamined: 2,
      alreadyHasObj: 0,
      inputStage: {
        stage: 'IXSCAN',
        nReturned: 2,
        executionTimeMillisEstimate: 31,
        works: 3,
        advanced: 2,
        needTime: 0,
        needYield: 0,
        saveState: 1,
        restoreState: 1,
        isEOF: 1,
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        },
        keysExamined: 2,
        seeks: 1,
        dupsTested: 0,
        dupsDropped: 0,
        peakTrackedMemBytes: 0
      }
    }
  },
  queryShapeHash: 'A93905E9C9869DA0264D6D85BC8875D4C698F973B857E2ABAAA6A355A5FCF0CB',
  command: {
    find: 'feedback',
    filter: {
      course_code: 'CS101'
    },
    '$db': 'college_nosql'
  },
  serverInfo: {
    host: 'JAGADEESWARI',
    port: 27017,
    version: '8.3.4',
    gitVersion: '4b03e7daaa316c78b9bf433046dba81637d581c0'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  ok: 1
}